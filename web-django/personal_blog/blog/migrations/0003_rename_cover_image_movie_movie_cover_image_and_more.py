# Generated by Django 4.2.5 on 2024-02-03 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_book_author_movie_director_serie_director_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='cover_image',
            new_name='movie_cover_image',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='created_at',
            new_name='movie_created_at',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='director',
            new_name='movie_director',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='rating',
            new_name='movie_rating',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='title',
            new_name='movie_title',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='updated_at',
            new_name='movie_updated_at',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='year',
            new_name='movie_year',
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_movie_title', to='blog.movie'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_movie_rating', to='blog.movie'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
