from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, MilkEntry, RateConfig

class FarmerSignUpForm(UserCreationForm):
    # Added initial='+91' here
    phone = forms.CharField(required=True, initial='+91', widget=forms.TextInput(attrs={'placeholder': '+91...'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'address')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_farmer = True
        if commit:
            user.save()
        return user

# --- NEW FORM FOR EDITING FARMER ---
class FarmerUpdateForm(forms.ModelForm):
    phone = forms.CharField(required=True, initial='+91')
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'address']

class MilkEntryForm(forms.ModelForm):
    class Meta:
        model = MilkEntry
        fields = ['farmer', 'date', 'shift', 'milk_type', 'fat', 'quantity']
        def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)

        # ✅ ONLY farmers in dropdown
         self.fields['farmer'].queryset = User.objects.filter(is_farmer=True)
        widgets = {
            'farmer': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'shift': forms.Select(attrs={'class': 'form-control'}),
            'milk_type': forms.Select(attrs={'class': 'form-control'}),
            'fat': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }

class RateForm(forms.ModelForm):
    class Meta:
        model = RateConfig
        fields = ['price_cow_fat', 'price_buffalo_fat']
        widgets = {
            'price_cow_fat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cow Rate'}),
            'price_buffalo_fat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Buffalo Rate'}),
        }