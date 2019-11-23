# pages/urls.py
from django.urls import path
from .views import HomePageView, SelectView, PostView, PostDetailView
urlpatterns = [
   path('', HomePageView.as_view(), name='home'),
   path('select/', SelectView.as_view(), name='select'),
   path('post/new/', PostView.as_view(), name='post_new'), # new
   path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

]
