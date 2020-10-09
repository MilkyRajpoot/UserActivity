from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.management import call_command
import json
import sys

# this class will load data from FIXTURE back to database .
class Command(BaseCommand):
	args = ''
	help = 'Loads the initial data in to database'
	def handle(self, *args, **options):
	        call_command('makemigrations')
	        call_command('migrate')
	        call_command('loaddata', 'FIXTURE/TestJSON.json',app_label='FIXTURE')
	#call_command('loaddata', 'peeldb/fixtures/countries.json', verbosity=0)
	        result = {'message': "Successfully loaded initial data"}
	        return json.dumps(result)