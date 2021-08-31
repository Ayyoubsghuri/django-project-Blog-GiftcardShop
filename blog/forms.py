from django import forms
from froala_editor.widgets import FroalaEditor

class PageForm(forms.ModelForm):
  content = forms.CharField(widget=FroalaEditor)