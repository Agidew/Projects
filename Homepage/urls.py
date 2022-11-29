
from django.urls import path,include
from Homepage.views import Home
from Homepage.views import About
from Homepage.views import contact

urlpatterns = [
    path('', Home,name='home'),
    path('about/', About,name='about'),
    path('contact/', contact,name='contact'),
    

]