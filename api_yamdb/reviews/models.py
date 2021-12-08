from django.db import models

class Category(models.Model):
    name = models.TextField('name', blank=False, max_length=256)
    slug = models.SlugField('slug', blank=False, max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.TextField('name', blank=False, max_length=256)
    slug = models.SlugField('slug', blank=False, max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField(
        'name',
        blank=False,
        max_length=256,
        db_index=True
    )
    year = models.IntegerField('year', blank=True)

    description = models.CharField(
        'description',
        max_length=256,
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        db_index=True,
        related_name='titles',
        verbose_name='genre'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='category'
    )

    def __str__(self):
        return self.name