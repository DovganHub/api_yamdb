from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, CommentsViewSet
from rest_framework.authtoken import views

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'^titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='review')
router_v1.register(r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentsViewSet, basename='comment')

#http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
]
