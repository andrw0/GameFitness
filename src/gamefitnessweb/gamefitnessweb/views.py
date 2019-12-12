from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, GameForm, ExercisesForm, FeedbackForm
from .models import games, exercises
from django.contrib.auth import authenticate
from django.views.generic.edit import FormView

class showUserForm(FormView):
    template_name= 'signin.html'
    form_class = UserForm
    success_url = 'homepage.html'

    def form_valid(self,form):
        form.save()
        return HttpResponseRedirect("../games")

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(request=self.request, form=form))
        #return HttpResponseRedirect('../homepage')


    # def get(self, form):
    # # if this is a POST request we need to process the form data
    #     if self.request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #         form = UserForm(request.POST)
    #     # check whether it's valid:
    #         if form.is_valid():
    #             form.save()
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponseRedirect('../')
    #
    # # if a GET (or any other method) we'll create a blank form
    #     else:
    #         form = UserForm()
    #
    #         return render(request, './gamefitnessweb/signin.html', {'form': form})

def homepage(request):
    return render(request,'homepage.html')

def showGameForm(request):
    form = GameForm()
    game = games.objects.all()
    args = {'form': form, 'game':game}
    return render(request, 'games.html', args)

def showExercisesForm(request):
    gameid = request.POST.get("game_id")
    form = ExercisesForm()
    allexerciseList = exercises.objects.all()
    args = {'form':form, 'exercisesList':allexerciseList, 'game_id':gameid}
    return render(request, 'exercisesList.html', args)
    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = ExercisesForm(request.POST)
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
    #     form = ExercisesForm()


def showFeedbackForm(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../homepage/')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


def auth_view(request):
    username = request.POST.get('email_address', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(email_address = email_address, password = password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('games.html')
    else:
        return HttpResponseRedirect('homepage.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect('homepage.html')
