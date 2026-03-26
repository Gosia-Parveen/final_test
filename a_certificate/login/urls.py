from . import views
from django.urls import path

urlpatterns = [
    path('',views.login_view, name='login'),
    path('user_dashboard/',views.user_dashboard, name='user_dashboard'),
    path('events/', views.events_page, name='events'),
    path('certificates/', views.certificates_page, name='certificates'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_event/', views.add_event, name='add_event'),
    path('add_participant/', views.add_participant, name='add_participant'),
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),

]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)