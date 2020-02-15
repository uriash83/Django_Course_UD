import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()

import random
from second_app.models import Topic,WebPage,AccessRecord
from faker import Faker

fakgen = Faker()
topics = ['Search','Social','Marketplace','New','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]# get_or_create zwraca  tuple i bierzemy  niego pierszy element [0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakgen.url()
        fake_date = fakgen.date()
        fake_name = fakgen.company()

        webpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == "__main__":
    print('populating')
    populate(20)
    print('popoulate finished')