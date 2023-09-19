from polls.models import Choice, Poll, Vote
from ecommerce.models import Product, Order
from django.contrib.auth.models import User
import datetime
import random
import time
from faker import Faker
fake = Faker()


def create_superuser():
    u = User.objects.create_user(
            first_name="admin",
            last_name="user",
            email="admin@django-quickstack.org",
            username="admin",
            password="password",
            is_superuser=True,
            is_staff=True
        )

def create_staffuser():
    u = User.objects.create_user(
            first_name="staff",
            last_name="user",
            email="staff1@django-quickstack.org",
            username="staff1",
            password="password",
            is_staff=True
        )
    u = User.objects.create_user(
            first_name="staff1",
            last_name="user",
            email="staff2@django-quickstack.org",
            username="staff2",
            password="password",
            is_staff=True
        )

def create_users(num_entries=5, overwrite=False):

    count = 0
    for _ in range(num_entries):
        first_name = fake.first_name()
        last_name = fake.last_name()
        u = User.objects.create_user(
            first_name="user",
            last_name="user",
            email="user" + str(count + 1) + "@django-quickstack.org",
            username="user" + str(count + 1 ),
            password="password"
        )
        count += 1


def create_polls(num_entries=5, choice_min=2, choice_max=5, overwrite=False):
    
    if overwrite:
        print('Overwriting polls')
        Poll.objects.all().delete()
    users = list(User.objects.filter(is_staff=False).all())
    count = 0
    for _ in range(num_entries):
        p = Poll(
            owner=random.choice(users),
            text=fake.paragraph(),
            pub_date=datetime.datetime.now()
        )
        p.save()
        num_choices = random.randrange(choice_min, choice_max + 1)
        for _ in range(num_choices):
            c = Choice(
                poll=p,
                choice_text=fake.sentence()
            ).save()
        count += 1

    Vote.objects.all().delete()
    users = User.objects.filter(is_staff=False).all()
    polls = Poll.objects.all()
    count = 0
    number_of_new_votes = users.count() * polls.count()
    for poll in polls:
        choices = list(poll.choice_set.all())
        for user in users:
            v = Vote(
                user=user,
                poll=poll,
                choice=random.choice(choices)
            ).save()
            count += 1


def create_products(num_entries=5, overwrite=False):
    
    if overwrite:
        print('Overwriting products')
        Product.objects.all().delete()
    count = 0
    for _ in range(num_entries):
        p = Product(
            name='Product Name ' + str(count + 1),
            image='product.png',
            description=fake.paragraph(),
        )
        p.save()
        count += 1

def create_all(num_entries=5, overwrite=False):
    
    create_superuser()
    create_staffuser()
    create_users(num_entries=5, overwrite=overwrite)

    create_polls()
    create_products()

    print("Done!")
