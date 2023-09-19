from django.shortcuts import render, redirect

from .models import ShippingWorkflow, WelcomeWorkflow

def workflow_list(request):
     context = {
          'shipping': ShippingWorkflow.objects.all(),
          'welcome': WelcomeWorkflow.objects.all(),
     }
     return render(request, 'state_machine_workflows/workflow_list.html', context)
