from django import forms
from .models import ChurnModel


class ChurnForm(forms.ModelForm):
    class Meta:
        model = ChurnModel
        fields = '__all__'
        widgets = {
            'Gender': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Male / Female'
            }),
            'Age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age'
            }),
            'MembershipType': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Free / Silver / Gold / Platinum'
            }),
            'PreferredCategory': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Men / Women / Kids / Beauty'
            }),
            'TotalOrders': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'TotalSpent': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any'
            }),
            'LastPurchaseDaysAgo': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'PurchaseFrequencyPerMonth': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any'
            }),
            'AppLoginFrequency': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'CouponUsageCount': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'ReturnCount': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'SatisfactionScore': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any'
            }),
        }
