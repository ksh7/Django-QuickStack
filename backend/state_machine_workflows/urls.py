from django.urls import path, include

from . import models
from . import views

app_label = "state_machine_workflows"

urlpatterns = [
    path('', views.workflow_list, name='workflow_list'),
    path('welcome/', include(models.WelcomeWorkflow.urls())),
    path('shipping/', include(models.ShippingWorkflow.urls())),
]