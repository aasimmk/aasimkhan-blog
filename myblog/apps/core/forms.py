from django import forms


class ContactForm(forms.Form):
    email_alt = forms.CharField(
        label='Email',
        widget=forms.EmailInput(attrs={
            "autocomplete": "false",
            "class": "doc",
            "placeholder": "Email",
            "tabindex": "1",
        }),
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "autocomplete": "off",
            "class": "doc",
            "placeholder": "Message",
            "tabindex": "2",
            "rows": "2",
        }),
        required=True
    )
    subject_1 = forms.CharField(required=False)  # Field #1 to identify bot
