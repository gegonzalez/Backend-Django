from django.urls import path

from .views import menu_index, menu_add, menu_details_uuid, option_add, option_edit
from .views import menu_order, order_add, order_details, order_index

app_name = 'menu'
urlpatterns = [
    path('', menu_index, name='index'),
    path('add/', menu_add, name='add'),
    path('<uuid:uuid>/details', menu_details_uuid, name='details_uuid'),
    path('<uuid:uuid>/option/add', option_add, name='option_add'),
    path('option/<uuid:uuid>/edit', option_edit, name='option_edit'),
    path('<uuid:uuid>', menu_order, name='order'),
    path('option/<uuid:uuid>/order', order_add, name='order_add'),
    path('order/<uuid:uuid>', order_details, name='order_details'),
    path('order/', order_index, name='order_index'),
]
