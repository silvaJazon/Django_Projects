from django.urls import path
from recipes.views import sobre,home,contact


urlpatterns = [
    path('sobre/', sobre),
    path('', home),
    path('contact/', contact),
]
