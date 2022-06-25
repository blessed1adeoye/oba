from django.urls import path
from . import views

app_name = 'af'

urlpatterns = [
    path('', views.home, name='amazon'),
    path('JUMIA/', views.jumia, name='jumia'),
    path('ADEOYE-BLESSED-OMOBUWA/', views.about, name='abo'),

]