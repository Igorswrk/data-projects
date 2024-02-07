from django.contrib import admin
from .models import (
    Movie,
    Review 
    # Serie, 
    # Book
)

# Register your models here.

class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0
    max_num = 1
    show_change_link = True


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines=[ReviewInline]
