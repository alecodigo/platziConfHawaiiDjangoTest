"""Views from Django"""

from django.shortcuts import render
from django.views.generic  import TemplateView

# Forms
from speaker.forms import SpeakerForm


class  PlatziConf(TemplateView):
    """View for PlatziConf"""

    template_name='base.html'

#class  PlatziConfSpeaker(TemplateView):
#    """View for Speakers"""

#   template_name = 'speaker.html'
    #form_class = SpeakerForm
