from django.urls import path

from .views import (
    HomePageView,
    MovieListView,
    # BookListView,
    # SerieListView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDetailView,
    ReviewDeleteView

)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('movie/', MovieListView.as_view(), name='movie'),
    # path('book/', BookListView.as_view(), name='book'),
    # path('serie/', SerieListView.as_view(), name='serie'),
    path('<slug:Title>/review/delete/', ReviewDeleteView.as_view(), name="review_delete"),
    path('<slug:Title>/review/edit/', ReviewUpdateView.as_view(), name="review_edit"),
    path('<slug:Title>/review/new/', ReviewCreateView.as_view(), name='review_new'),
    path('<slug:Title>/review/', ReviewDetailView.as_view(), name='review_detail'),

]