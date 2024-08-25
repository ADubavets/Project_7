from django.shortcuts import render, redirect
from .models import ComputerisationTechnical


def show_all(request):
    computerisation_technicals = ComputerisationTechnical.objects.all().order_by("price")
    return render(request,
                  'app_1/show_all.html',
                  {'computerisation_technicals': computerisation_technicals})


def show_item(request, item_id):
    item = ComputerisationTechnical.objects.get(pk=item_id)
    return render(request,
                  'app_1/show_item.html',
                  {'item': item})


def main(request):
    return redirect('main')


def error_404(request, *args, **argv):
    return redirect('main')


def error_500(request, *args, **argv):
    return redirect('main')
