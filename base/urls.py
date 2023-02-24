from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lga/', views.lga, name='lga'),
    path('polling_unit_result/<int:uniqueid>/', views.polling_unit_result, name='polling_unit_result'),
    path('lga_result/<str:lga_name>/<int:lga_id>/', views.lga_result_details, name='lga_result_details'),
    path('add_polling_unit_result/', views.add_polling_unit_result, name='new_polling_unit'),

]