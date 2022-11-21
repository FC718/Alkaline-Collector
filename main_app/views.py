from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView,UpdateView, DeleteView

from django.views.generic import ListView, DetailView

from .models import Alkaline, Fruit

from .forms import JuicingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def alkaline_index(request):
    alkalines = Alkaline.objects.all()
    return render(request, 'alkaline/index.html',  {
        # left is the key and the right is the value.
        # 'key': value
        'alkalines': alkalines
    })

def alkalines_detail(request, alkaline_id):
    alkaline = Alkaline.objects.get(id=alkaline_id)
    # First, create a list of the fruit ids that alkaline DOES have
    id_list = alkaline.fruits.all().values_list('id')
    # query for the fruits that the alkaline list doesnt have


    # instantiate JuicingForm to be rendered
    juicing_form = JuicingForm()
    return render(request, 'alkaline/detail.html', {
        'alkaline': alkaline, 'juicing_form': juicing_form 
    })

class AlkalineCreate(CreateView):
    model = Alkaline
    fields = ['name', 'type', 'description', 'benefits']


class AlkalineUpdate(UpdateView):
    model = Alkaline
    fields = ['name', 'type', 'description', 'benefits']

class AlkalineDelete(DeleteView):
    model = Alkaline
    success_url = '/alkaline'

def add_juicing(request, alkaline_id):
    #create a ModelForm instance using
    #the data that was submitted in the form
    form = JuicingForm(request.POST)
    # validate the form
    if form.is_valid():
        # We want a model instance, but 
        # we can't save to the db yet
        # because we have no assigned the
        # alkaline_id FK.
        new_juicing = form.save(commit=False)
        new_juicing.alkaline_id = alkaline_id
        new_juicing.save()
    return redirect('detail', alkaline_id=alkaline_id)

class FruitList(ListView):
  model = Fruit

class FruitDetail(DetailView):
  model = Fruit

class FruitCreate(CreateView):
  model = Fruit
  fields = '__all__'

class FruitUpdate(UpdateView):
  model = Fruit
  fields = ['name', 'color']

class FruitDelete(DeleteView):
  model = Fruit
  success_url = '/fruits'

    