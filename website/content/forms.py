from django import forms
from .models import News, About, ContactData


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'text',)


class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = ('title', 'text',)


class ContactDataForm(forms.ModelForm):

    class Meta:
        model = ContactData
        fields = ('title', 'text',)


class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)

