from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, GameForm, ExercisesForm, FeedbackForm
from .models import games

def showUserForm(request):
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
            return HttpResponseRedirect('../')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, './gamefitnessweb/signin.html', {'form': form})

def homepage(request):
    return render(request,'./gamefitnessweb/homepage.html')

def showGameForm(request):
    form = GameForm()
    game = games.objects.all()
    args = {'form': form, 'game':game}
    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = GameForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         form.save()
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponse("Thank You")
    #
    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = GameForm()

    return render(request, './gamefitnessweb/games.html', args)

def showExercisesForm(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ExercisesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("Thank You")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExercisesForm()

    return render(request, './gamefitnessweb/exercisesList.html', {'form': form})

def showFeedbackForm(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../')
    else:
        form = FeedbackForm()
    return render(request, './gamefitnessweb/feedback.html', {'form': form})
