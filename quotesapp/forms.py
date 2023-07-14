from django.forms import ModelForm, CharField, DateField, TextInput, DateInput, ModelChoiceField
from .models import Author, Tag, Quote


class AuthorForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    birthdate = DateField(required=True, widget=DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))
    birthplace = CharField(max_length=100, required=True, widget=TextInput())
    description = CharField(required=True, widget=TextInput())
    
    class Meta:
        model = Author
        fields = ['name', 'birthdate', 'birthplace', 'description']

class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']

class QuoteForm(ModelForm):

    author = ModelChoiceField(queryset=Author.objects, required=True, to_field_name='name')
    quote = CharField(required=True, widget=TextInput)

    class Meta:
        model = Quote
        fields = ['author', 'quote']