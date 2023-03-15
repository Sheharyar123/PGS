from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-4", "placeholder": "Your Name"}
        ),
    )
    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-4", "placeholder": "Your Email"}
        ),
    )
    message = forms.CharField(max_length=1000, required=True, widget=forms.Textarea)
    message.widget.attrs.update(
        {"class": "form-control mb-4", "placeholder": "Your Message"}
    )
