from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() == 'z':
        raise forms.ValidationError('NAME DONT NEED START WITH Z')

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                  widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])
    #botcatcher wyłapuje czy jakiś bot nie tylke klika w stronę co czy jakiś bot nie wpisuje dane w input. 
    # botcatcher jest inputem więc jesli bot też coś tu wpisze to bot złapany

    def clean(self): # czyści wszystko = że ma dostęp, clean_name czyści name
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError('EMAILS ARE NOT THE SAME')

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError('GOTCHA BOT!')
        return botcatcher
