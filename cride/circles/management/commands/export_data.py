"""Custom Command"""
#django
from django.core.management.base import BaseCommand, CommandError

#Circle model
from cride.circles.models import Circle
#Script
from export_csv import ExportData

class Command(BaseCommand):
  help = 'Load csv data'
  def handle(self, *args, **options):
    #try:
    ExportData()
    #except:
    #  raise CommandError('something goes wrong')
    
    self.stdout.write(self.style.SUCCESS('the data was load'))

