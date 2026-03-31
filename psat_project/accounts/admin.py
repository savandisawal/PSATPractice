from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from .models import UserProfile


class AdminUserCreationForm(forms.ModelForm):
    """Custom add-user form for admin: username + email only, no password."""
    email = forms.EmailField(required=True, label='Email address')

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user with that email already exists.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_unusable_password()
        if commit:
            user.save()
        return user


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fields = ['role', 'approved', 'grade']
    readonly_fields = []


class UserAdmin(BaseUserAdmin):
    add_form = AdminUserCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email'),
        }),
    )
    inlines = [UserProfileInline]
    list_display = ['username', 'email', 'is_active', 'get_approved', 'get_role', 'date_joined']
    list_filter = ['is_active', 'profile__approved', 'profile__role']
    actions = ['approve_users', 'reject_users']

    def get_approved(self, obj):
        return obj.profile.approved if hasattr(obj, 'profile') else False
    get_approved.boolean = True
    get_approved.short_description = 'Approved'

    def get_role(self, obj):
        if obj.is_staff:
            return 'admin'
        return obj.profile.role if hasattr(obj, 'profile') else '-'
    get_role.short_description = 'Role'

    def approve_users(self, request, queryset):
        for user in queryset:
            user.is_active = True
            user.save()
            if hasattr(user, 'profile'):
                user.profile.approved = True
                user.profile.approval_date = timezone.now()
                user.profile.save()
            send_mail(
                subject='Your PSAT Practice Account Has Been Approved!',
                message=(
                    f"Hi {user.username},\n\n"
                    f"Great news! Your PSAT Practice account has been approved.\n"
                    f"You can now log in at: http://localhost:8000/accounts/login/\n\n"
                    f"Good luck with your studies!"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=True,
            )
        self.message_user(request, f'{queryset.count()} user(s) approved and notified.')
    approve_users.short_description = 'Approve selected users'

    def reject_users(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f'{queryset.count()} user(s) rejected.')
    reject_users.short_description = 'Reject selected users'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
