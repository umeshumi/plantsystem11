from django.shortcuts import render
from .models import Plant
from .forms import GrainForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def homePage(request):
	return render(request, 'home.html')

def plantList(request):
	plants = Plant.objects.all()
	page = request.GET.get('page')
	paginator = Paginator(plants, 4)

	try:
		plantss = paginator.get_page(page)
	except PageNotAnInteger:
		plantss = paginator.get_page(1)
	except EmptyPage:
		plantss = paginator.get_page(paginator.num_pages)
	context = {'plant':plantss}
	return render(request, 'plantlist.html', context)

def plantDetails(request, plantid):
	plants = Plant.objects.filter(id=plantid)
	context = {'plant':plants}
	return render(request, 'plantDetails.html', context)

def addGrain(request):
	 if request.method == "POST":
	 	form = GrainForm(request.POST, request.FILES)
	 	if form.is_valid():
	 		form.save()
	 		return redirect('plantcategory:plantlist')
	 else:
	 	form = GrainForm()
	 return render(request, 'addgrain.html', {'form': form})