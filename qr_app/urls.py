from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import os
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('qr_generator/', views.generate_qr_page, name='generate_qr_page'),
    path('generate/', views.generate_qr_codes, name='generate_qr_codes'),
    path('compose/', views.compose_message, name='compose_message'),
    path('qr/<str:unique_key>/enter/', views.enter_message_page, name='enter_message'),
    path('qr/<str:unique_key>/save/', views.save_message, name='save_message'),
    path('qr/<str:unique_key>/display/', views.display_message_page, name='display_message'),
    path('qr/<str:unique_key>/download/', views.download_qr, name='download_qr'),
]

# ✅ React frontend fallback route (uncommented & enabled)
urlpatterns += [
    re_path(
        r'^(?!admin/|login/|qr_generator/|generate/|compose/|qr/|assets/|media/).*$',  # exclude Django routes
        views.react_app  # Make sure this view renders your index.html
    ),
]

# ✅ Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(
        '/assets/',
        document_root=os.path.join(settings.BASE_DIR, 'frontend', 'dist', 'assets')
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
