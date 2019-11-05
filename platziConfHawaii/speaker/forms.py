"""Speaker Forms"""

# from django
from django.forms import ModelForm
from speaker.models import Speaker

class  SpeakerForm(ModelForm):
	"""Spearker Form"""
	class Meta:
		model = Speaker
		fields = ('first_name', 'last_name', 'topic')

