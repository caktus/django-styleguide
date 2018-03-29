from django import forms


class EverythingBagelForm(forms.Form):

    BAGEL_CHOICES = (
    (1, "12 Grain"),
    (2, "Asiago Parmesan"),
    (3, "Blueberry"),
    (4, "Cinnamon Raisin"),
    (5, "Cinnamon Sugar"),
    (6, "Egg"),
    (7, "Pumpkin – Fall Special!"))

    text = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput())
    disabled_text = forms.CharField(
        widget=forms.TextInput(attrs={'disabled': 'disabled'})
    )
    readonly_text = forms.CharField(
        widget=forms.TextInput(attrs={'readonly':'readonly'})
    )
    text_with_error = forms.CharField(label='Phone Number')
    checkbox1 = forms.BooleanField()
    checkbox2 = forms.BooleanField()
    select = forms.ChoiceField(choices=[('',  "Select an Option"), (1, 'one'), (2, 'two'), (3, 'three')])
    radio = forms.ChoiceField(choices=[(1, 'one'), (2, 'two'), (3, 'three')], widget=forms.RadioSelect())
    file = forms.FileField(label='Upload Your Photo')
    search = forms.CharField(label='Search', widget=forms.TextInput(attrs={'placeholder':'Search'}))
    select = forms.ChoiceField(choices=BAGEL_CHOICES, required=True) # label="", initial='', widget=forms.Select(),

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

create_user_form_initial = {
    "email": "tom@example.com",
}
