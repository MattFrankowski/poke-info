from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_pokemon


class PokemonView(TemplateView):
    template_name = "pokeinfo/pokemon.html"

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        pokemon_name = self.kwargs["name"]
        # add pokemon info to context
        context["pokemon"] = get_pokemon(pokemon_name)
        return context
