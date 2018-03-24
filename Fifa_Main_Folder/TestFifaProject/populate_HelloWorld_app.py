import os


import django
django.setup()

## Faker population JavaScript
import random
from HelloWorld_app.models import Topic, AccessRecord, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marktplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
     for entry  in range(N):

         # get topic
         top = add_topic()

         # create the fake data for that entry
         fake_url = fakegen.url()
         fake_date = fakegen.date()
         fake_name = fakegen.company()

         # create new webpage entry
         webpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

         #create fake acces record for the website above
         acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':

    print("Start populating script ...")
    settings.configure()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestFifaProject.settings.py')
    django.setup()
    populate(20)
    print("Population completed.")
