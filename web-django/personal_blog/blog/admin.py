from django.contrib import admin
from .models import (
    Movie,
    Review 
    # Serie, 
    # Book
)

# Register your models here.

admin.site.register(Review)
# admin.site.register(Serie)
admin.site.register(Movie)
# admin.site.register(Book)