from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .services import get_pokemon
from .forms import SearchPokemonForm


class PokemonView(TemplateView):
    """
    View detailed Pokemon information.
    """
    template_name = "pokeinfo/pokemon.html"

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        pokemon_name = self.kwargs["name"]
        # add pokemon info to context
        context["pokemon"] = get_pokemon(pokemon_name)
        return context


class IndexView(FormView):
    """
    Display search Pokemon form.
    """
    template_name = "pokeinfo/index.html"
    form_class = SearchPokemonForm

    def get_success_url(self):
        return f'/pokemon/{self.request.POST.get("name").lower()}/'

