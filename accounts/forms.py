from django import forms
from .models import RepairmanProfile

class RepairmanProfileForm(forms.ModelForm):
    class Meta:
        model = RepairmanProfile
        fields = [
            'skills',
            'experience_years',
            'price_per_service',
            'availability',
            'nid_number',
            'documents',
        ]
