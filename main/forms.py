from django import forms
from .models import GetIntouch


class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = GetIntouch
        fields = '__all__'
        #fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(GetInTouchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name