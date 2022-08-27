from django.urls import path
from blog.views import BlogPostDetail, BlogPostList, BlogPostCreate, BlogPostUpdate, BlogPostDelete


app_name = "blog"

urlpatterns = [
    path("blogpost/<int:pk>/detail", BlogPostDetail.as_view(), name="blogpost-detail"),
    path("blogpost/create", BlogPostCreate.as_view(), name="blogpost-create"),
    path("blogpost/<int:pk>/update", BlogPostUpdate.as_view(), name="blogpost-update"),
    path("blogpost/<int:pk>/delete", BlogPostDelete.as_view(), name="blogpost-delete"),
    path("blogpost/list", BlogPostList.as_view(), name="blogpost-detail-list"),
]


