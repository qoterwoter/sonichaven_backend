from django import forms
from .models import Arrangement

class GenreForm(forms.ModelForm):
    genre_choices = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[],
    )

    class Meta:
        model = Arrangement
        fields = ('genre_choices',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Arrangement.objects.order_by().values_list('genre', flat=True).distinct()
        self.fields['genre_choices'].choices = [(genre, genre) for genre in genres]
