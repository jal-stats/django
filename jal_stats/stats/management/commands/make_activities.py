# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import json
# from random import choice
from faker import Faker


class Command(BaseCommand):

    def handle(self, *args, **options):
        '''Make some fake activities'''
        fake = Faker()
        activities = []

        for _ in range(10):
            activity = {
                'model': 'stats.Activity',
                'fields': {
                    # 'user': user
                    'full_description': fake.bs(),
                    'units': fake.word(),
                }
            }
            activities.append(activity)

                        # 'timestamp': str(datetime.utcfromtimestamp(
                        #     int(row['Timestamp']))),

        with open('stats/fixtures/activities.json', 'w') as f:
            f.write(json.dumps(activities))
