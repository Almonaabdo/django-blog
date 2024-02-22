from django.contrib import admin
from django.urls import path, include
from users import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('blog.urls'), name="blog-home" ),
    path('register/', user_view.Register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html', redirect_authenticated_user=True), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    #path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password-reset"),
    #path('password-reset/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_reset_done.html'), name="password-reset-done"),
    #path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password-reset-confirm"),

    path('profile/', user_view.Profile, name="profile"),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)