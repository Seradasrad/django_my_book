from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns +=[re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
               re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
               re_path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
               re_path(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),

               ]