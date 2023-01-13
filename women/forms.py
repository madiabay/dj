from django import forms
from women import models

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=200)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField()
    cat = forms.ModelChoiceField(queryset=models.Category.objects.all())
