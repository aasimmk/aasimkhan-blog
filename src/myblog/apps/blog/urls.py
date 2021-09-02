from django.urls import path

from blog.views import ListBlog, ListBlogCategory, ListBlogByCategory, ListBlogByYear, BlogDetailView, SearchBlog


app_name = 'blog'

urlpatterns = (
    path('', ListBlog.as_view(), name='list_blog'),
    path('category/', ListBlogCategory.as_view(), name='list_blog_category'),
    path('category/<str:slug>/', ListBlogByCategory.as_view(), name='view_blogs_by_category'),
    path('<int:year>/', ListBlogByYear.as_view(), name='view_blog_by_year'),
    path('<str:slug>/', BlogDetailView.as_view(), name='view_blog_detail'),
    path('search/', SearchBlog.as_view(), name='search')
)
