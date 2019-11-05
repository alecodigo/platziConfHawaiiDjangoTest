"""Speaker Forms"""

# from django
from django import forms
from models import Speaker

class  SpeakerForm(forms.Form):
	"""Spearker Form"""
	class Meta:
		model = Speaker
		fields = ('first_name', 'last_name', 'topic')

