from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegistrationForm, LoginForm


def _is_staff(user):
    return user.is_active and user.is_staff


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Notify admins via email
            admin_emails = list(
                User.objects.filter(is_staff=True).values_list('email', flat=True)
            )
            if admin_emails:
                send_mail(
                    subject='New PSAT Student Registration — Approval Needed',
                    message=(
                        f"A new student has registered and needs your approval.\n\n"
                        f"Username: {user.username}\n"
                        f"Email: {user.email}\n\n"
                        f"Log in to the admin panel to approve: http://localhost:8000/admin/auth/user/{user.pk}/change/"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=admin_emails,
                    fail_silently=True,
                )
            messages.success(
                request,
                'Account created! An admin will review and approve your account. '
                'You will receive an email once approved.',
            )
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.is_active:
                messages.error(
                    request,
                    'Your account is pending admin approval. Please check back later.',
                )
            else:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                if user.is_staff:
                    return redirect('pending_approvals')
                return redirect('dashboard')
        else:
            messages.error(request, 'No account found with that username and email.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/?logged_out=1')


@login_required
@user_passes_test(_is_staff)
def pending_approvals(request):
    pending = User.objects.filter(is_active=False, is_staff=False).order_by('date_joined')
    return render(request, 'accounts/pending_approvals.html', {'pending': pending})


@login_required
@user_passes_test(_is_staff)
def approve_student(request, user_id):
    student = get_object_or_404(User, pk=user_id, is_active=False, is_staff=False)
    student.is_active = True
    student.save()
    # Update profile if it exists
    if hasattr(student, 'userprofile'):
        student.userprofile.approved = True
        student.userprofile.save()
    send_mail(
        subject='Your PSAT Practice account has been approved!',
        message=(
            f"Hi {student.username},\n\n"
            f"Your account has been approved. You can now log in at http://localhost:8000/accounts/login/"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[student.email],
        fail_silently=True,
    )
    messages.success(request, f'{student.username} has been approved.')
    return redirect('pending_approvals')
