from django.urls import path
from . import views
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views



app_name = "user"

urlpatterns = [
    path('',views.loginin,name='index'),
    path('signup/',views.signup,name='signup'),
    path('signup/<str:ref_code>/' ,views.signup,name='signup_ref'),
    path('forget-password',views.forgetpass,name='forgetpass'),
    path('waitadmin' ,views.waitadmin,name='waitadmin'),
    path('dashboard/' ,views.dash,name='dash'),
    path('logout/' ,views.logout_vi,name='logout'),

    # path('c455b964453d80b4afc9aa08de1a636e.txt', views.read_file,name=''),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="user/forget-password.html",email_template_name='user/email.html',success_url = reverse_lazy('user:password_reset_done')),
    name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="user/forget-password-done.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="user/forget-password-reset.html",success_url = reverse_lazy('user:password_reset_complete')),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="user/waitadmin.html"),name="password_reset_complete"),





]

