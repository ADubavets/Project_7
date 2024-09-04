from django.shortcuts import render, redirect
from .models import ComputerisationTechnical
from .forms import UpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.core.paginator import Paginator


def show_all(request):
    com_tex_all = ComputerisationTechnical.objects.all().order_by("-price")
    paginator = Paginator(com_tex_all, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,
                  'app_1/show_all.html',
                  {'computerisation_technicals': page_obj})


def show_admin_all(request):
    form = UpdateForm()
    com_tex_all = ComputerisationTechnical.objects.all().order_by("-parse_datetime")
    paginator = Paginator(com_tex_all, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # computerisation_technicals = ComputerisationTechnical.objects.all().order_by("-parse_datetime")
    return render(request,
                  'app_1/show_admin_item.html',
                  {
                      'form': form,
                      'computerisation_technicals': page_obj
                  })


def show_item(request, item_id):
    item = ComputerisationTechnical.objects.get(pk=item_id)
    return render(request,
                  'app_1/show_item.html',
                  {'item': item})


def update_item(request, item_id):
    if request.method == 'POST':
        new_description = dict(request.POST).get('description', '')
        new_price = dict(request.POST).get('price', '')
        ComputerisationTechnical.objects.filter(pk=item_id).update(
            price=new_price[0],
            description=new_description[0]
        )
    return redirect('items_admin')


def delete_item(request, item_id):
    ComputerisationTechnical.objects.filter(pk=item_id).delete()
    return redirect('items_admin')


def main(request):
    return redirect('main')


def error_404(request, *args, **argv):
    return redirect('main')


def error_500(request, *args, **argv):
    return redirect('main')


def login(request):
    return render(request, 'app_1/login.html')


def logout_view(request):
    LogoutView(request)


class SingUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
