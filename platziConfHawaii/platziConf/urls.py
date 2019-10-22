"""Users URls."""

# Django

from django.urls import path 

from platziConf import views


urlpatterns = [

        # home
        path(
                '',
                view=views.home,
                name='home-view',
            ),
       
    ]
