from django import forms
from db_file_storage.form_widgets import DBClearableFileInput, \
    DBAdminClearableFileInput
from .models import Doc

class DocForm(forms.ModelForm):
    class Meta(object):
        model = Doc
        exclude = []
        widgets = {
            'picture': DBClearableFileInput,
        }
