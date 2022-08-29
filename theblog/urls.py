from django.urls import path
from .views import AddPostView, AdminView, ContactUser, ArticleDetailView, HomeView, AddPostView, UpdatePostView, DeletePostView, CategoryView, LikeView, CategoryListView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('admin_view/', AdminView.as_view(), name="admin_view"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('contact_user/', ContactUser.as_view(), name="contact_user"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/edit/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    #path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
    path('like/<int:pk>', LikeView, name="like_post"),


]
