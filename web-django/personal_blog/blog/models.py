from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField
# Create your models here.


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True, name="id")
    movie_created_at = models.DateTimeField(auto_now_add=True)
    movie_updated_at = models.DateTimeField(auto_now=True)

    movie_cover_image = models.ImageField(upload_to='static\media\movie_covers', null=True, blank=True)

    movie_title = models.CharField(max_length=100, name="Title")
    movie_director = models.CharField(max_length=100, null=True, blank=True, name="Director")
    movie_year = models.IntegerField(name="Year")
    movie_rating = models.DecimalField(max_digits=3, decimal_places=1, name="Rating")

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"title": self.Title})
    
# class Book(models.Model):
#     id = models.IntegerField(primary_key=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

#     title = models.CharField(max_length=100, null=True, blank=True)
#     author = models.CharField(max_length=100, null=True, blank=True)
#     year = models.IntegerField()
#     rating = models.DecimalField(max_digits=3, decimal_places=1)

#     def __str__(self):
#         return f"{self.title} teste"

# class Serie(models.Model):
#     id = models.IntegerField(primary_key=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

#     title = models.CharField(max_length=100)
#     director = models.CharField(max_length=100, null=True, blank=True)
#     year = models.IntegerField()
#     rating = models.DecimalField(max_digits=3, decimal_places=1)

#     def __str__(self):
#         return self.title


class Review(models.Model):

    # Associe a revisão a um livro, filme ou série
    # book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True, blank=True)
    # serie = models.ForeignKey('Serie', on_delete=models.CASCADE, null=True, blank=True)

    video_review = EmbedVideoField()
    text_review = models.TextField()

    # # movie = models.ForeignKey(Movie, auto_created=True, on_delete=models.CASCADE, null=True, blank=True, related_name="movie_movie_title")
    # # book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    # # serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True, blank=True)
    # # rating = models.ForeignKey(Movie, auto_created=True, on_delete=models.CASCADE, related_name="movie_movie_rating")

    # # video_review = models.URLField()
    # # text_review = models.TextField()

    def __str__(self):
        return f"{self.movie.Title} review"

    def save(self, *args, **kwargs):
        if self.movie:
            self.title = self.movie.Title
            self.rating = self.movie.Rating
            
            super().save(*args, **kwargs)
            
        # elif self.serie:
        #     self.rating = self.serie.rating
        #     self.title = self.serie.title
        # if self.book:
        #     self.rating = self.book.rating
        #     self.title = self.book.title

    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"title": self.movie.Title})   
        


