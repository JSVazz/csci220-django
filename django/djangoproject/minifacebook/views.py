from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Status

@cache_page(60 * 15)
def index(request):
    context = {"statuses": Status.objects.order_by('-date_time')[:10]}
    return render(request, "index.html", context)


