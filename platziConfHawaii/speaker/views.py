"""Views from Django"""

from django.shortcuts import render
from django.views.generic  import TemplateView

# Forms
from . import SpeakerForm





class  PlatziConf(TemplateView):
	"""View for PlatziConf"""

	template_name='base.html'

class  PlatziConfSpeaker(TemplateView):
	"""View for Speakers"""

	template_name = 'speaker/speaker.html'
	form_class = SpeakerForm

