from django import forms
from crispy_forms.helper import FormHelper


class SearchPokemonForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'e.g. Charizard'}))

    # hide SearchPokemonForm label
    def __init__(self, *args, **kwargs):
        super(SearchPokemonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False