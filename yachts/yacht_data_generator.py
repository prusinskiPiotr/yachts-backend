"""
file for generating large amount of dummy data
it uses Faker library for generating realistic data
it has to be run from python manage.py shell
TODO write user does not exist exception for yacht creation
TODO optionally generate fixtures
"""
import random
from django.contrib.auth.models import User
from yachts.models import Yacht
from faker import Faker

faker = Faker()
user = User.objects.get(username='admin')


users = User.objects.create(username=faker.simple_profile()['username'], email=faker.simple_profile()['mail'],first_name=faker.first_name(), last_name=faker.last_name(), password="1qaz@WSX")
yachts = Yacht.objects.create(model_name=" ".join(faker.words(2)), length=random.randint(1, 30), width=random.randint(1, 15), year=faker.year(), max_crew=random.randint(1, 10), berths=random.randint(1, 10), owner=User.objects.get(id=random.randint(1, 50)))