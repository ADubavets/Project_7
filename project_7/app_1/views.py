from django.shortcuts import render
from .models import ComputerisationTechnical


def show_all(request):
    computerisation_technicals = ComputerisationTechnical.objects.all().order_by("price")
    return render(request,
                  'app_1/show_all.html',
                  {'computerisation_technicals': computerisation_technicals})
