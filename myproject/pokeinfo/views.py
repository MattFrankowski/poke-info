from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib import messages
from .services import get_pokemon
from .forms import SearchPokemonForm
import json


# class PokemonView(TemplateView):
#     """
#     View detailed Pokemon information.
#     """
#     template_name = "pokeinfo/pokemon.html"
#
#     def get_context_data(self, *args, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         pokemon_name = self.kwargs["name"]
#         # add pokemon info to context
#         context["pokemon"] = get_pokemon(pokemon_name)
#         return context


def pokemonView(request, name):
    try:
        pokemon = get_pokemon(name)
    except json.JSONDecodeError:
        messages.error(request, "Pokémon not found.")
        return redirect("index")

    context = {
        "pokemon": pokemon
    }

    return render(request, "pokeinfo/pokemon.html", context)


class IndexView(FormView):
    """
    Display search Pokemon form.
    """
    template_name = "pokeinfo/index.html"
    form_class = SearchPokemonForm

    def get_success_url(self):
        return f'/pokemon/{self.request.POST.get("name").lower()}/'

