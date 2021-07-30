from django import forms
from django.forms import ModelForm, fields
from . models import Comment

class CommentForm(ModelForm):
    text = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        "class":"form-control", "rows":"3", "placeholder":"Join the discussion and leave a comment!"
    }))
    class Meta:
        model = Comment
        fields = ['text', ]