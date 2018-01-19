from django import forms

class EverythingBagelForm(forms.Form):
    text = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput())
    disabled_text = forms.CharField(disabled=True)
    readonly_text = forms.CharField(
        widget=forms.TextInput(attrs={'readonly':'readonly'})
    )
    text_with_error = forms.CharField(label='Phone Number')
    checkbox1 = forms.BooleanField()
    checkbox2 = forms.BooleanField()
    select = forms.ChoiceField(choices=[('',  "Select an Option"), (1, 'one'), (2, 'two'), (3, 'three')])
    radio = forms.ChoiceField(choices=[(1, 'one'), (2, 'two'), (3, 'three')], widget=forms.RadioSelect())
    file = forms.FileField(label='Upload Your Photo')

everything_bagel_form_initial = {
    "text": "",
    "disabled_text": "This field can't be changed",
    "readonly_text": "This field is read only",
    "text_with_error": "32-43564"
}

class CreateUserForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'readonly': 'readonly', }))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'required': 'required', }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'required': 'required', }))

    def clean(self):
        for field_name, field in self.fields.items():
            if field_name in self._errors:
                field.widget.attrs['errors'] = ' '.join(self._errors[field_name])

create_user_form_initial = {
    "email": "tom@example.com",
}
