from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<blog_id>' ,views.detail, name='detail'),
    # path('new', views.new, name='new'),
    # path('create', views.create, name='create'),
    path('newblog', views.blogpost, name='newblog'),
    path('delete/<blog_id>', views.delete, name='delete'),
    path('edit/<blog_id>', views.edit, name='edit'),
]