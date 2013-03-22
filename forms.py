from django import forms
from spacescout_admin.models import QueuedSpace


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='Select a file',
        help_text='csv, xls, or xlsx files, please'
    )


class QueueForm(forms.ModelForm):
    class Meta:
        model = QueuedSpace
