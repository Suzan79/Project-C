from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from users import views as user_views
from .forms import UpdatedLoginForm
from .views import ArtistCard , isartist , artist_register_info, artistAllApplications , artistDetailApplications, rejectArtistApplication ,approveArtistApplication
from . import views


urlpatterns = [
    path('register/', user_views.register, name='register_page'),
    path('register/artist', isartist, name='register_artist_page'),
    path('register/artist-info', artist_register_info, name='register_artist_info'),
    path('administrator/', artistAllApplications.as_view(), name='administrator'),
    path('administrator/<int:pk>/', artistDetailApplications.as_view(), name='detail_artist_application'),
    path('administrator/<int:pk>/reject', rejectArtistApplication.as_view(), name='reject_artist_application'),
    path('administrator/<int:pk>/approve', approveArtistApplication.as_view(), name='approve_artist_application'),
    path('profile/', user_views.profile, name='profile_page'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=UpdatedLoginForm), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout_page'),
    re_path('password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    re_path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name="registration/change_password.html"), name='change_password'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name="registration/password_change_done.html"), name='password_change_done'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    re_path(r'^activate_email/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate_email, name='activate_email'),
    path('artist/<int:pk>/', ArtistCard.as_view(), name='artist_card'),

]
