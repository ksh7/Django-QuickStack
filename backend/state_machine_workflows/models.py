from django.db import models

# Create your models here.
from django.core.mail import send_mail
from joeflow.models import Workflow
from joeflow import tasks

class ShippingWorkflow(Workflow):

    # model fields to store the state
    email = models.EmailField(blank=True)
    shipping_address = models.TextField()
    tracking_code = models.TextField()

    # tasks (nodes)
    checkout = tasks.StartView(fields=["shipping_address", "email"])

    ship = tasks.UpdateView(fields=["tracking_code"])

    def has_email(self):
        if self.email:
            return [self.send_tracking_code]

    def send_tracking_code(self):
        send_mail(
            subject="Your tracking code",
            message=self.tracking_code,
            from_email=None,
            recipient_list=[self.email],
        )

    def end(self):
        pass

    # edges
    edges = [
        (checkout, ship),
        (ship, has_email),
        (has_email, send_tracking_code),
        (has_email, end),
        (send_tracking_code, end),
    ]

    class Meta:
        app_label  = 'state_machine_workflows'


class WelcomeWorkflow(Workflow):
    # state
    user = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    # behavior
    start = tasks.StartView(fields=["user"])

    def has_user(self):
        if self.user:
            return [self.send_welcome_email]
        else:
            return [self.end]

    def send_welcome_email(self):
        self.user.email_user(
            subject="Welcome", message="Hello %s!" % self.user.get_short_name(),
        )

    def end(self):
        pass

    edges = [
        (start, has_user),
        (has_user, end),
        (has_user, send_welcome_email),
        (send_welcome_email, end),
    ]

    class Meta:
        app_label  = 'state_machine_workflows'

