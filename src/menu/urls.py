from django.urls import path

from .views import menu_index, menu_add, menu_details_uuid, option_add, option_edit

app_name = 'menu'
urlpatterns = [
    path('', menu_index, name='index'),
    path('add/', menu_add, name='add'),
    path('<uuid:uuid>/details', menu_details_uuid, name='details_uuid'),
    path('<uuid:uuid>/option/add', option_add, name='option_add'),
    path('option/<uuid:uuid>/edit', option_edit, name='option_edit'),
]
