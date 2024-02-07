from django import forms


class TemplateForm(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Subject = forms.CharField()
    Message = forms.CharField(widget=forms.Textarea)
