from django.db import models
from django.urls import reverse

# Create your models here.


class Movie(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    cover_image = models.ImageField(upload_to='movie_covers/', null=True, blank=True)

    title = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title

    
class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    title = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title


class Serie(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    title = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.TextField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True, blank=True)
    
    video_review = models.URLField()
    text_review = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if self.book:
            self.rating = self.book.rating
            self.title = self.book.title
        elif self.movie:
            self.rating = self.movie.rating
            self.title = self.movie.title
        elif self.serie:
            self.rating = self.serie.rating
            self.title = self.serie.title

        super().save(*args, **kwargs)
    