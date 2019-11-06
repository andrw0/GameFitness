from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm, GameForm

def get_userForm(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("Thank You")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'signin.html', {'form': form})

def homepage(request):
    return render(request,'homepage.html')

def get_gameForm(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("Thank You")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, '.gameshtml', {'form': form})
