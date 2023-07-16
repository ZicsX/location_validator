from django.shortcuts import render
from .forms import UrlForm
from .models import Store

def home(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            # scraping
            # validation

            return render(request, 'stores/result.html')
    else:
        form = UrlForm()

    return render(request, 'stores/home.html', {'form': form})

def result(request):
    all_stores = Store.objects.all()
    verified_stores = Store.objects.filter(is_verified=True)
    flagged_stores = Store.objects.filter(is_verified=False)

    context = {
        'all_stores': all_stores,
        'verified_stores': verified_stores,
        'flagged_stores': flagged_stores,
    }

    return render(request, 'stores/result.html', context)
