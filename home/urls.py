
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.test,name='test'),
    path('login/', views.loginpage, name='login'),
    path('signup/', views.signuppage, name='signup'),
    path('homePage/',views.homepage, name='homepage'),
    path('homePage/uploadimage/', views.upload_image, name='upload_image'),
    path('logout/', views.logout_page, name='logout'),
    path('homePage/update_user/', views.user_update, name='user_update'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)
     
urlpatterns += staticfiles_urlpatterns()