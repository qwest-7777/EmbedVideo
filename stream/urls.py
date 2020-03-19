from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video/<int:pk>/', views.VideoDetailView.as_view(), name='video_detail'),
    path('view_order/', views.view_order, name='view_order'),
    path('all_videos_date/', views.all_videos_date, name='all_videos_date'),
    path('all_videos_popular/', views.all_videos_popular, name='all_videos_popular'),
    path('admin2/', views.admin2, name='admin2'),
    path('admin2/video/', views.admin2_videos, name='admin2_videos'),
    path('admin2/category/<int:pk>/', views.category_video, name='category_video'),
    path('admin2/video_add/', views.VideoCreateView.as_view(), name='video_add'),
    path('admin2/video_edit/<int:pk>/', views.VideoEditView.as_view(), name='video_edit'),
    path('admin2/video_delete/<int:pk>/', views.VideoDeleteView.as_view(), name='video_delete'),
    path('admin2/categories/', views.categories, name='admin2_categories'),
    path('admin2/category_add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('admin2/category_edit/<int:pk>/', views.CategoryEditView.as_view(), name='category_edit'),
    path('admin2/category_delete/<int:pk>/', views.CategoryCreateView.as_view(), name='category_delete'),
]
