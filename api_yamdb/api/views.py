from rest_framework import filters, mixins, status, viewsets
from reviews.models import Genre, Title
from reviews.models import Category
from reviews.serializers import CategorySerializer, GenreSerializer, TitleSerializer
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()#.order_by('id')
    serializer_class = CategorySerializer
    # permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()#.order_by('id')
    serializer_class = GenreSerializer
    # permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()#.order_by('id')
    serializer_class = TitleSerializer
    # permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    lookup_field = 'slug'