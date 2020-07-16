import os
import csv

from cride.circles.models import Circle

def ExportData():
  result = []
  data = open('circles.csv')
  rows = csv.reader(data)
  for row in rows:
    result.append(row)
    print(row)

  for row in result[1:]:
    info = Circle(
    name=row[0], 
    slug_name=row[1],
    is_public=int(row[2]),
    verified=int(row[3]),
    members_limit=int(row[4])      
    )
    info.save()
    print(info)

