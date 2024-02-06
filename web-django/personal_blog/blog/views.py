from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import (
    Movie,
    # Book, 
    # Serie, 
    Review
)

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class MovieListView(ListView):
    model = Movie
    template_name = 'movie.html'
    fields = ['movie_title', 'movie_director', 'movie_year', 'movie_rating']
    context_object_name = 'movies'


# class BookListView(ListView):
#     model = Book
#     template_name = 'book.html'
#     context_object_name = 'books'


# class SerieListView(ListView):
#     model = Serie
#     template_name = 'serie.html'
#     context_object_name = 'series'


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review_detail.html'
    fields = ['video_review', 'text_review']
    context_object_name = 'review'

class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review_new.html'
    fields = ['video_review', 'text_review']
    success_url = reverse_lazy('review_detail')

class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'review_edit.html'
    fields = ['video_review', 'text_review']
    success_url = reverse_lazy('review_detail')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_delete.html'
    success_url = reverse_lazy('home')
