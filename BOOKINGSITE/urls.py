from django.contrib import admin
from django.urls import path
from home import views
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('login',views.login),
    path('signup',views.signup),
    path('profile',views.profile),
    path('logout',views.logout),
    path('password',views.password),
    path('superuser',views.super),
    path('laptop',views.lap),
    path('mobile',views.mob),
    path('camera',views.camera),
    path('smartwatch',views.smartwatch),
    path('others',views.others),
    path('save',views.save_data),
    path('news1',views.news1),
    path('news2',views.news2),
    path('news3',views.news3),
    path('news4',views.news4),
    path('news5',views.news5),
    path('news6',views.news6),
    path('news7',views.news7),
    path('news8',views.news8),
    path('news9',views.news9),
    path('news10',views.news10),
]
 
 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)