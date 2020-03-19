from django import forms
from django.contrib.admin import widgets as adminWidget

class VideoForm(forms.Form):
    title = forms.CharField(max_length=100)
    url = forms.CharField(max_length=100)
    description = forms.CharField(
        max_length=500,
        widget=forms.Textarea(),
        help_text='Write here your description!'
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        title = cleaned_data.get('title')
        url = cleaned_data.get('url')
        description = cleaned_data.get('description')
        if not title and not url and not description:
            raise forms.ValidationError('You have to write something!')