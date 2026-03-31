from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('test/start/<slug:subject_slug>/', views.start_test, name='start_test'),
    path('test/<int:attempt_id>/', views.take_test, name='take_test'),
    path('test/<int:attempt_id>/save/', views.save_answer, name='save_answer'),
    path('test/<int:attempt_id>/submit/', views.submit_test, name='submit_test'),
    path('results/<int:attempt_id>/', views.test_results, name='test_results'),
    path('history/', views.history, name='history'),
]
