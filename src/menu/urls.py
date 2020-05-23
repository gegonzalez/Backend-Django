from django.urls import path

from .views import menu_index, menu_details, menu_add, menu_details_uuid

app_name = 'menu'
urlpatterns = [
    path('', menu_index, name='index'),
    path('add/', menu_add, name='add'),
    path('<int:menu_id>', menu_details, name='details'),
    path('<uuid:uuid>', menu_details_uuid, name='details_uuid'),
]
