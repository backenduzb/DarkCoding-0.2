from django.urls import path
from .views import Home,Posts,AddPost
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',Home.as_view(),name="home"),
    path('blogs/',Posts.as_view(),name="blogla"),
    path('post/add/', AddPost.as_view(), name='add_post'),  
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)