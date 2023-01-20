from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from women import models

# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     slug = forms.SlugField(max_length=255)
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
#     is_published = forms.BooleanField()
#     cat = forms.ModelChoiceField(queryset=models.Category.objects.all())


class AddPostForm(forms.ModelForm):

    class Meta:
        model = models.Women
        fields = ('__all__')

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 150:
            raise ValidationError('LIMIT 200')

        return title


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()