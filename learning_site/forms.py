from django import forms
from django.core import validators

# Custom Validator
def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')

# this one is to show a custom validation,
# preferred is to use validators=[validators.MaxLengthValidator(0)]
class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="Leave empty",
                               validators=[must_be_empty]
                               )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                "You need to enter the same email in both fields")

    # - - - This is a beginner way to handle honeypot
    # def clean_honeypot(self):
    #     honeypot = self.cleaned_data['honeypot']
    #     if len(honeypot):
    #         raise forms.ValidationError(
    #             "honeypot should be left empty. Bad bot!")
    #     return honeypot
