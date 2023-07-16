from django.shortcuts import redirect, render
from .models import Store
from .scraper import scrape_store_data

def home(request):
    if request.method == 'POST':
        url = request.POST['url']
        scrape_store_data(url)
        
        return redirect('result')
    else:
        return render(request, 'stores/home.html')

def result(request):
    stores = Store.objects.all()
    verified_stores = Store.objects.filter(is_verified=True)
    flagged_stores = Store.objects.filter(is_verified=False)

    context = {
        'stores': stores,
        'verified_stores': verified_stores,
        'flagged_stores': flagged_stores,
    }

    return render(request, 'stores/result.html', context)
