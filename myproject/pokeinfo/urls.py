from django.urls import path
from .views import pokemonView, IndexView

urlpatterns = [
    # Pokemon detail view
    path('pokemon/<str:name>/', pokemonView, name="pokemon"),
    # Index view with pokemon search form
    path('', IndexView.as_view(), name="index")
]