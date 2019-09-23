using python3.6 and ubuntu 18.04
create new virtualenv called env in project root
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

for data generation, type
```
python manage.py shell
```
this will open interactive python shell, now type following code:
```
import random
from django.contrib.auth.models import User
from yachts.models import Yacht, Rental
from faker import Faker

faker = Faker()

# change values in range() to change the amount of data generated
# (1, 100) will produce 100 objects
for i in range(1, 100):
    User.objects.create(username=faker.simple_profile()['username'], email=faker.simple_profile()['mail'],first_name=faker.first_name(), last_name=faker.last_name(), password="1qaz@WSX")
    Yacht.objects.create(model_name=" ".join(faker.words(2)), length=random.randint(1, 30), width=random.randint(1, 15), year=faker.year(), max_crew=random.randint(1, 10), berths=random.randint(1, 10), owner=User.objects.get(id=random.randint(5, 50)))
    Rental.objects.create(from_date=str(faker.future_date(end_date="+30d", tzinfo=None)), to_date=str(faker.future_date(end_date="+45d", tzinfo=None)), insurance=random.choice([True, False]), yacht=Yacht.objects.get(id=random.randint(1, 400)), user=User.objects.get(id=random.randint(5, 50)))
```

