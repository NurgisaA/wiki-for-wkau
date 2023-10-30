from django import forms


class EntryForm(forms.Form):
    title = forms.CharField(max_length=20, label="title")
    content = forms.CharField(widget=forms.Textarea, label="Content")
