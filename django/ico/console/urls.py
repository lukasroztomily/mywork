
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_admin, name='home_admin'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('user_admin/', views.user_admin, name='user_admin'),
    path('add_user/', views.add_user, name='add_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('remove_user/<int:user_id>/', views.remove_user, name='remove_user'),
    path('approve_user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('blocked_user/<int:user_id>/', views.blocked_user, name='blocked_user'),
    path('unblocked_user/<int:user_id>/', views.unblocked_user, name='unblocked_user'),
    path('waiting_approve_user/', views.waiting_approve_user, name='waiting_approve_user'),
    path('blog_admin/', views.blog_admin, name='blog_admin'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('blog_list_published/', views.blog_list_published, name='blog_list_published'),
    path('list_blocked_user/', views.list_blocked_user, name='list_blocked_user'),
    path('remove_blog/<int:blog_id>/', views.remove_blog, name='remove_blog'),
    path('unpublished_blog/<int:blog_id>/', views.unpublished_blog, name='unpublished_blog'),
    path('published_blog/<int:blog_id>/', views.published_blog, name='published_blog'),
    
    path('logout/', views.logout_admin, name='logout_admin'),

]
