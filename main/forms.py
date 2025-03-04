from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    source_page = forms.CharField(widget=forms.HiddenInput())  # Hidden field

    class Meta:
        model = Enquiry
        fields = ['first_name', 'last_name', 'phone', 'email', 'category', 'course', 'message']

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name.isalpha():
            raise forms.ValidationError("First name should contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name.isalpha():
            raise forms.ValidationError("Last name should contain only letters.")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Enquiry.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if Enquiry.objects.filter(phone=phone).exists():
            raise forms.ValidationError("This phone number is already registered.")
        return phone




from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"



# from django import forms
# from .models import Payment

# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = Payment
#         fields = [
#             "first_name", "last_name", "phone", "email", "gender", "aadhar",
#             "address", "state", "city", "zip_code", "course", "fees"
#         ]


# from django import forms
# from .models import Payment

# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = Payment
#         fields = [
#             "first_name", "last_name", "phone", "email", "gender", "aadhar",
#             "address", "state", "city", "zip_code", "course", "fees"
#         ]



from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            "first_name", "last_name", "phone", "email", "gender", "aadhar",
            "address", "state", "city", "zip_code", "course", "fees"
        ]
