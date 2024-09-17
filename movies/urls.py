from django.urls import path
from .import views
from .views import (
    PostListView,
    PostDetailView,
)
 
urlpatterns = [
    path('', PostListView.as_view(), name='movies-home'),
    path('about/', views.about, name='movies-about'),
    path('movie/<int:pk>/', PostDetailView.as_view(), name='movie_detail'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('already_booked/', views.already_booked, name='already_booked'),
    path('profile/balance/', views.updatebalance, name='balance')
]


'''path('movie/book/<int:movie_id>/', views.book_movie, name='bookingmovie')
'''
'''
from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostListView, name='movies-home'),
    path('about/', views.about, name='movies-about'),
    path('movie/<int:pk>/', views.PostDetailView, name='movie_detail'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('already_booked/', views.already_booked, name='already_booked'),
]
'''