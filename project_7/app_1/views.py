from django.shortcuts import render, redirect
from .models import ComputerisationTechnical
from .forms import UpdateForm


def show_all(request):
    computerisation_technicals = ComputerisationTechnical.objects.all().order_by("-price")
    return render(request,
                  'app_1/show_all.html',
                  {'computerisation_technicals': computerisation_technicals})


def show_admin_all(request):
    form = UpdateForm()
    computerisation_technicals = ComputerisationTechnical.objects.all().order_by("-parse_datetime")
    return render(request,
                  'app_1/show_admin_item.html',
                  {
                      'form': form,
                      'computerisation_technicals': computerisation_technicals
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
    return redirect('admin')


def delete_item(request, item_id):
    ComputerisationTechnical.objects.filter(pk=item_id).delete()
    return redirect('admin')


def main(request):
    return redirect('main')


def error_404(request, *args, **argv):
    return redirect('main')


def error_500(request, *args, **argv):
    return redirect('main')
