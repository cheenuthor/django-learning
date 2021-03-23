from django.urls import path
from . import views


urlpatterns = [
    path("", views.StartingPage.as_view(), name="starting-page"),
    path("posts", views.AllPost.as_view(), name="posts-page"),
    # ?/posts/my-first-post(eg : slug)
    path("post/<slug:slug>", views.PostDetail.as_view(),
         name="post-detail-page")

]
