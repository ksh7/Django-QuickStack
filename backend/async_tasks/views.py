from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse


from . import forms
from . import tasks
from . import models

def list_tasks(request):
    context = {
          'websitefootprint': models.WebsiteCarbonFootprint.objects.all(),
          'coffeepicture': models.CoffeePicture.objects.all(),
     }
    return render(request, 'async_tasks/list_tasks.html', context)

@login_required
def website_carbon_footprint(request):
    if request.method == 'POST':
        form = forms.WebsiteCarbonFootprintdForm(request.POST)
        if form.is_valid:
            tasks.calculate_website_carbon_footprint.delay(request.POST['url'])

            messages.success(request, "Task submitted successfully. It may take several seconds for external API to respond.", extra_tags='alert alert-success alert-dismissible fade show')

            return redirect('async_tasks:website_carbon_footprint')
    else:
        form = forms.WebsiteCarbonFootprintdForm()
    context = {
        'form': form,
    }
    return render(request, 'async_tasks/add_carbon_footprint_task.html', context)


@login_required
def get_coffee_picture(request):
    tasks.fetch_random_coffee_picture.delay()
    messages.success(request, "Task submitted successfully. It may take several seconds for external API to respond.", extra_tags='alert alert-success alert-dismissible fade show')
    return redirect('async_tasks:list_tasks')


def get_latest_coffee_picture(request):
    _object = models.CoffeePicture.objects.latest('id')
    if _object:
        messages.success(request, "Keep refreshing page till async API gets latest Coffee picture.", extra_tags='alert alert-success alert-dismissible fade show')
        context = {
            'object': _object,
        }
        return render(request, 'async_tasks/show_coffee_picture.html', context)
    else:
        return "No pictures available. Try after sometime."