from django import forms
from .models import Plant


class GrainForm(forms.ModelForm):
	class Meta:
		model = Plant
		fields = '__all__'
