from django.shortcuts import render

# Create your views here.

from django.views.generic  import TemplateView


class  PlatziConf(TemplateView):
	"""View for PlatziConf"""

	template_name='base.html'

