from django import forms

# define from
class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False, widget=forms.Textarea)