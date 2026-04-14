from django import forms
from .models import ChurnModel


class ChurnForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    MEMBERSHIP_CHOICES = [
        ('', 'Select Membership Type'),
        ('Free', 'Free'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
    ]

    CATEGORY_CHOICES = [
        ('', 'Select Preferred Category'),
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Kids', 'Kids'),
        ('Beauty', 'Beauty'),
        ('Footwear', 'Footwear'),
    ]

    Gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    MembershipType = forms.ChoiceField(
        choices=MEMBERSHIP_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    PreferredCategory = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = ChurnModel
        fields = '__all__'
        labels = {
            'Gender': 'Gender',
            'Age': 'Age',
            'MembershipType': 'Membership Type',
            'PreferredCategory': 'Preferred Category',
            'TotalOrders': 'Total Orders',
            'TotalSpent': 'Total Spent',
            'LastPurchaseDaysAgo': 'Last Purchase (Days Ago)',
            'PurchaseFrequencyPerMonth': 'Purchase Frequency / Month',
            'AppLoginFrequency': 'App Login Frequency',
            'CouponUsageCount': 'Coupon Usage Count',
            'ReturnCount': 'Return Count',
            'SatisfactionScore': 'Satisfaction Score',
        }
        widgets = {
            'Age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age'
            }),
            'TotalOrders': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 12'
            }),
            'TotalSpent': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',
                'placeholder': 'e.g. 12500.50'
            }),
            'LastPurchaseDaysAgo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 30'
            }),
            'PurchaseFrequencyPerMonth': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',
                'placeholder': 'e.g. 0.68'
            }),
            'AppLoginFrequency': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 8'
            }),
            'CouponUsageCount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 3'
            }),
            'ReturnCount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 1'
            }),
            'SatisfactionScore': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',
                'placeholder': 'e.g. 4.5'
            }),
        }
