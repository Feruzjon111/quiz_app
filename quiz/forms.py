from django import forms
from .models import Test

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['baza', 'savol', 'a', 'b', 'c', 'd', 'togri']
        widgets = {
            'savol': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'a': forms.TextInput(attrs={'class': 'form-control'}),
            'b': forms.TextInput(attrs={'class': 'form-control'}),
            'c': forms.TextInput(attrs={'class': 'form-control'}),
            'd': forms.TextInput(attrs={'class': 'form-control'}),
            'togri': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 1, 'placeholder': 'a, b, c yoki d'}),
            'baza': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'savol': 'Savol matni',
            'a': 'Variant A',
            'b': 'Variant B',
            'c': 'Variant C',
            'd': 'Variant D (ixtiyoriy)',
            'togri': 'To‘g‘ri javob (a/b/c/d)',
            'baza': 'Baza',
        }

