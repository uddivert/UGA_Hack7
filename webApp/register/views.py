from django.shortcuts import render
from django.http import HttpResponseRedirect
from webApp.appForms.RegisterForm import RegisterForm


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            print(form.data)
            return HttpResponseRedirect('../../home/')

    else:
        form = RegisterForm()

    return render(request, 'register/register.html', {'form': form})


