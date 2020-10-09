from django.utils import timezone
from UserActivityPeriodApp.models import *
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.management import call_command
import json
import sys

#Via this class will dump the data from database to db.json file present in FIXTURE.
class Command(BaseCommand):
    args = ''
    help = 'Loads the initial data in to database'
    def handle(self, *args, **options):
            sysout = sys.stdout
            sys.stdout = open('FIXTURE/db.json', 'w')
            call_command('dumpdata')
            sys.stdout = sysout
            result = {'message': "Successfully dumping initial data"}
            return json.dumps(result)