from django.urls import path

from .views import (
    HomePageView,
    MovieListView,
    # BookListView,
    # SerieListView,
    # ReviewCreateView,
    # ReviewUpdateView,
    ReviewDetailView
    # ReviewDeleteView

)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('movies/', MovieListView.as_view(), name='movies'),
    # path('book/', BookListView.as_view(), name='book'),
    # path('serie/', SerieListView.as_view(), name='serie'),
    # path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name="review_delete"),
    # path('review/<int:pk>/edit/', ReviewUpdateView.as_view(), name="review_edit"),
    # path('review/new/', ReviewCreateView.as_view(), name='review_new'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),

]