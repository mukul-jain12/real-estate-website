from django.conf.urls import url
from basic_app import views

# Template urls!
app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^home/', views.home, name='home'),
    url(r'^overview/', views.overview, name='overview'),
    url(r'^location/', views.location, name='location'),
    url(r'^amenities/', views.amenities, name='amenities'),
    url(r'^specification/', views.specification, name='specification'),
    url(r'^about_the_partners/', views.about_the_partners, name='about_the_partners'),
]
