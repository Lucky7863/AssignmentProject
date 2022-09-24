from django.urls import path
from BooksApp.views import (
    InsertJsonApiView, GetTitleProductView, GetBooksdetailsView, GetEditApiView)

urlpatterns = [
    path('api/', InsertJsonApiView),
    path('find_items/', GetBooksdetailsView, name="find_items"),
    path('show_product/<int:pk>/', GetTitleProductView, name="show_product"),
    path('edit_post_request/<int:pk>/', GetEditApiView, name="edit_post_request"),

]
