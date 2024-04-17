from django.urls import path
from store import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('register/',views.RegView.as_view(),name="register"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('movie/<int:pk>/',views.MovieView.as_view(),name="movie"),
    path('moviedetail/<int:pk>/',views.MovieDetailView.as_view(),name="movie_detail"),
    path('watchlist/<int:pk>/',views.WatchListView.as_view(),name="watchlist"),
    path('watchlistdetail/',views.WatchListDetail.as_view(),name="watchlist_detail"),
    path('deletewatchlist/<int:pk>/',views.WatchListDelete.as_view(),name="delete_watchlist"),
    
 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)