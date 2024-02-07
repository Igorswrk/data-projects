from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField
# Create your models here.


class Movie(models.Model):

    movie_created_at = models.DateTimeField(auto_now_add=True)
    movie_updated_at = models.DateTimeField(auto_now=True)

    movie_cover_image = models.ImageField(upload_to='static\media\movie_covers', null=True, blank=True)

    movie_title = models.CharField(max_length=100)
    movie_director = models.CharField(max_length=100, null=True, blank=True)
    movie_year = models.IntegerField(name="Year")
    movie_rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.movie_title

    def get_absolute_url(self):
        return reverse("movies", kwargs={"pk": self.pk})
    

class Review(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)

    video_review = EmbedVideoField()
    text_review = models.TextField()

    def get_absolute_url(self):
        return reverse(f"review_detail", kwargs={"pk": self.pk})  


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

