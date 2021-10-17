from django import forms
from .models import Post
from crispy_forms.helper import Formhelper
from crispy_forms.layout import Submit, Layout, Field


class PostForm(forms.Modelform):
    helper = Formhelper()