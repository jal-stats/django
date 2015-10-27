from django.core.management.base import BaseCommand
from faker import Faker
import json
from random import random
from stats.models import Activity



class Command(BaseCommand):

    def handle(self, *args, **options):
        '''Make some fake activities'''
        fake = Faker()
        datapoints = []

        for activity in Activity.objects.all():
            for _ in range(random.randint(3, 35)):
                datapoint = {
                    'model': 'stats.Datapoint',
                    'fields': {
                        'activity': activity,
                        'reps': random.randint(0, 30),
                        'date': fake.date(),
                    }
                }
                datapoints.append(datapoint)

                        # 'timestamp': str(datetime.utcfromtimestamp(
                        #     int(row['Timestamp']))),

        with open('stats/fixtures/datapoints.json', 'w') as f:
            f.write(json.dumps(datapoints))
