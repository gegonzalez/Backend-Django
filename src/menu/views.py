from uuid import uuid1
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Menu, Option, Order
from .forms import MenuForm, OptionForm, OrderForm

@login_required(login_url="/accounts/login")
def menu_index(request):
    """
    Returns a list of Menus with date greater or iqual than today
    """
    today = datetime.date.today()
    menu_list = Menu.objects.filter(published_date__gte=today).order_by('published_date')

    return render(request, 'menu_index.html', {'menu_list': menu_list})

@login_required(login_url="/accounts/login")
def menu_add(request):
    """
    Validates te request to add a new Menu or return the found validations
    """
    if request.method == 'POST':
        form = MenuForm(request.POST)

        if form.is_valid():
            published_date = form.cleaned_data['publishedDateInput']

            Menu.objects.create(uuid=uuid1(), published_date=published_date).save()
            return redirect('menu:index')
    else:
        form = MenuForm()

    return render(request, 'menu_add.html', {'form': form})

@login_required(login_url="/accounts/login")
def option_add(request, uuid):
    """
    Validates the request to add a new Option or return the found validations
    """
    if request.method == 'POST':
        form = OptionForm(request.POST)

        if form.is_valid():
            description = form.cleaned_data['description']

            menu = Menu.objects.filter(uuid=uuid)
            Option.objects.create(menu_id=menu[0].id, description=description, uuid=uuid1()).save()
            return redirect('menu:details_uuid', uuid)
    else:
        form = OptionForm()

    return render(request, 'option_add.html', {'form': form})

@login_required(login_url="/accounts/login")
def option_edit(request, uuid):
    """
    Validates the request to edit an Option or return the found validations
    """
    option = get_object_or_404(Option, uuid=uuid)

    if request.method == 'POST':
        form = OptionForm(request.POST)

        if form.is_valid():
            option.description = form.cleaned_data['description']
            option.save()
            return redirect('menu:details_uuid', option.menu.uuid)
    else:
        form = OptionForm(data={'description':option.description})

    context = {'form': form, 'option': option}
    return render(request, 'option_details.html', context)

def menu_details_uuid(request, uuid):
    """
    Search a Menu and its Options by an uuid
    """
    menu    = get_object_or_404(Menu, uuid=uuid)
    options = Option.objects.filter(menu_id=menu.id)

    context = {'menu': menu, 'options': options}

    return render(request, 'menu_details.html', context)

def menu_order(request, uuid):
    """
    Search a Menu and its Options by an uiid
    Validates the time limit to display the Menu
    """
    if is_in_todays_time_limit():
        menu = get_object_or_404(Menu, uuid=uuid)
        context = {'menu': menu}
    else:
        context = {'error_message': 'It is not possible to recieve your Order after 11 AM'}

    return render(request, 'order.html', context)

def order_add(request, uuid):
    """
    Creates an Order. Validates the time limit to create the order
    """
    error_message = None
    option = get_object_or_404(Option, uuid=uuid)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if is_in_todays_time_limit() and form.is_valid():
            order = Order.objects.create(option=option, uuid=uuid1(), **form.cleaned_data)
            order.save()
            return redirect('menu:order_details', order.uuid)
        error_message = 'It is not possible to recieve your Order after 11 AM'
    else:
        form = OrderForm()

    return render(request,
                  'order_add.html',
                  {'form': form, 'option': option, 'error_message': error_message})

def order_details(request, uuid):
    """
    Search a Menu and its Options by an uiid
    """
    order = get_object_or_404(Order, uuid=uuid)

    return render(request, 'order_details.html', {'order': order})

def is_in_todays_time_limit():
    """
    Compares current time against the today time limit
    """
    limit_time_string = "11:00:00"

    limit_time_datetime = datetime.datetime.strptime(limit_time_string, "%H:%M:%S")

    current_datetime = datetime.datetime.today()
    today_time_limit = current_datetime.replace(hour=limit_time_datetime.time().hour,
                                                minute=limit_time_datetime.time().minute,
                                                second=limit_time_datetime.time().second,
                                                microsecond=0)

    return current_datetime < today_time_limit

@login_required(login_url="/accounts/login")
def order_index(request):
    """
    Lists the Orders of the current day
    """
    today = datetime.date.today()
    order_list = Order.objects.filter(option__menu__published_date=today).order_by('id')

    return render(request, 'order_index.html', {'order_list': order_list})
