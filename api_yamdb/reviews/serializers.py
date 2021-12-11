from rest_framework import serializers

from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Genre
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(read_only=True,
                                            slug_field='username')

    genre = serializers.SlugRelatedField(read_only=True,
                                         slug_field='username')

    class Meta:
        fields = ('__all__')
        model = Title
        lookup_field = 'slug'
