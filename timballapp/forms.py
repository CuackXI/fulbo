from django import forms


class activateRequest(forms.Form):
    name = forms.CharField(label="Introducí texto para confirmar la request que diga la url",
                           max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))


class barraBusqueda(forms.Form):
    query = forms.CharField(label="", max_length=200, widget=forms.TextInput(
        attrs={'class': 'input-search', 'placeholder': 'Buscar...'}))
