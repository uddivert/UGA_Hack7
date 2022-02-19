from django.shortcuts import render
from django.http import HttpResponseRedirect
from webApp.appForms.RegisterForm import RegisterForm
from webApp.register.models import RegisterModel


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            model = RegisterModel(new_name=form.data['name'])
            model.save()
            print(model.new_name)
            print(RegisterModel.objects.all())

            return HttpResponseRedirect('/home/')

    else:
        form = RegisterForm()

    return render(request, 'register/register.html', {'form': form})


