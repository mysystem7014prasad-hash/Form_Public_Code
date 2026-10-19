from django import forms


class DetailsForm(forms.Form):
    rollno = forms.CharField(
        max_length=5,
        min_length=5,
        label="Roll No"
    )

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)
    course = forms.CharField(max_length=100)