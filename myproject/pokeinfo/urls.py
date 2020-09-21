from django.urls import path
from .views import PokemonView, IndexView

urlpatterns = [
    # Pokemon detail view
    path('pokemon/<str:name>/', PokemonView.as_view(), name="pokemon"),
    # Index view with pokemon search form
    path('', IndexView.as_view(), name="index")
]