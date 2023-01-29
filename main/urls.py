from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryView.as_view(), name="category_list"),
    path('category/<int:pk>/', BlogCategoryView.as_view(), name="filtered_blog_list"),
    path('blog/', BlogListView.as_view(), name="blog_list"),
]