from django.urls import path,include

from posts.views import Post,PostCreate,PostDetail,PostDelete,PostEdit

urlpatterns = [
    path('',Post.as_view(),name='post'),
    path('<int:pk>/edit',PostEdit.as_view(),name='edit'),
    path('<int:pk>/delete',PostDelete.as_view(),name='delete'),
    path('<int:pk>',PostDetail.as_view(),name='detail'),
    path('new/',PostCreate.as_view(),name='new'),
]