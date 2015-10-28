from datetime import datetime
from django.core.management.base import BaseCommand
from faker import Faker
import json
from random import random
from stats.models import Activity



class Command(BaseCommand):

    def handle(self, *args, **options):
        '''Make some fake activities'''
        fake = Faker()
        stats = []

        for activity in Activity.objects.all():
            for _ in range(random.randint(3, 35)):
                stat = {
                    'model': 'stats.Stat',
                    'fields': {
                        'activity': activity,
                        'reps': random.randint(0, 30),
                        'date': datetime.date(fake.date_time_this_year()),
                    }
                }
                stats.append(stat)

                        # 'timestamp': str(datetime.utcfromtimestamp(
                        #     int(row['Timestamp']))),

        with open('stats/fixtures/stats.json', 'w') as f:
            f.write(json.dumps(stats))
