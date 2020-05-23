from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect

from .models import Menu, Option
from .forms import MenuForm


def menu_index(request):
    """
    Returns a list of Menus with date greater or iqual than today
    """
    today = datetime.today()
    menu_list = Menu.objects.filter(published_date__gte=today).order_by('published_date')

    return render(request, 'menu_index.html', {'menu_list': menu_list})

def menu_details(request, menu_id):
    """
    Search a Menu and its Options by an id
    """
    menu    = get_object_or_404(Menu, id=menu_id)
    options = Option.objects.filter(menu_id=menu_id)

    context = {'menu': menu, 'options': options}

    return render(request, 'menu_details.html', context)

def menu_add(request):
    """
    Validates te request to add a new Menu or return the found validations
    """
    form = MenuForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('menu:index')

    return render(request, 'menu_add.html', {'form': form})

def menu_details_uuid(request, uuid):
    """
    Search a Menu and its Options by an uuid
    """
    menu = get_object_or_404(Menu, uuid=uuid)
    options = Option.objects.filter(menu_id=menu.menu_id)

    context = {'menu': menu, 'options': options}

    return render(request, 'menu_details.html', context)
