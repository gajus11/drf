from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter

# Create router and register viewsets with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSets)
router.register(r'users', views.UserViewSets)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]