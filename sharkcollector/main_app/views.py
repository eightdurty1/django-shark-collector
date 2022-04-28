from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shark, Toy
from .forms import FeedingForm

# Create your views here.
# defining the home view
# class Shark:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# sharks = [
#   Shark('Thor', 'Scalloped Hammer Headshark', 'Bites', 12),
#   Shark('Spots', 'Leopard Shark', 'Docile towards people', 8),
#   Shark('Raven', 'Swell Shark', 'If threateaned, well bend into U and swell up', 20),
# ]

from django.shortcuts import render
from .models import Shark

class SharkUpdate(UpdateView):
  model = Shark
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class SharkDelete(DeleteView):
  model = Shark
  success_url = '/sharks/'

class SharkCreate(CreateView):
    model = Shark
    fields = '__all__'
    success_url = '/sharks/'


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def sharks_index(request):
    sharks = Shark.objects.all()
    return render(request, 'sharks/index.html', {'sharks': sharks})
    
def sharks_detail(request, shark_id):
  shark = Shark.objects.get(id=shark_id)
  # Get the toys the shark doesn't have
  toys_shark_doesnt_have = Toy.objects.exclude(id__in = shark.toys.all().values_list('id'))
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'sharks/detail.html', {
    # include the cat and feeding_form in the context
    'shark': shark, 'feeding_form': feeding_form,
    # Add the toys to be displayed
    'toys': toys_shark_doesnt_have
  })

# add this new function below cats_detail
def add_feeding(request, shark_id):
  # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.shark_id = shark_id
        new_feeding.save()
    return redirect('detail', shark_id=shark_id)

def assoc_toy(request, shark_id, toy_id):
  Shark.objects.get(id=shark_id).toys.add(toy_id)
  return redirect('detail', shark_id=shark_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'