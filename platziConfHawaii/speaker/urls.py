"""Speaker URL """


from django.urls import path
from speaker import views

urlpatterns = [

	path(
		route='',
		view=views.PlatziConf.as_view(),
		name='home'
	 ),

]
