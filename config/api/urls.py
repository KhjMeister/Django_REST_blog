from django.urls import include, path

  

urlpatterns = [
    path('posts/', include('api.posts.urls')),
    path('comments/', include('api.comments.urls')),
]