# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    lesson = forms.CharField()
    date = forms.CharField()
    homework = forms.CharField()
    submit = forms.CharField()
    deadline = forms.CharField()
    valid = forms.CharField()
