from datetime import datetime
from django.core.management.base import BaseCommand
from faker import Faker
import json
from random import randint
from stats.models import Activity



class Command(BaseCommand):

    def handle(self, *args, **options):
        '''Make some fake activities'''
        fake = Faker()
        stats = []


        for activity in Activity.objects.all():
            for n in range(randint(3, 10), randint(12, 28)):
                stat = {
                    'model': 'stats.Stat',
                    'fields': {
                        'activity': activity.pk,
                        'reps': randint(0, 30),
                        'date': str(datetime.date(datetime(2015, 10, n))),
                    }
                }
                stats.append(stat)

                        # 'timestamp': str(datetime.utcfromtimestamp(
                        #     int(row['Timestamp']))),

        with open('stats/fixtures/stats.json', 'w') as f:
            f.write(json.dumps(stats))
