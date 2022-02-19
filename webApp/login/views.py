from django.shortcuts import render
from django.http import HttpResponseRedirect
from webApp.appForms.LoginForm import LoginForm


def login(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            return HttpResponseRedirect('/home/')

    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})

