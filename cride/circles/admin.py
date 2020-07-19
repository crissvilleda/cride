"""Circles admin"""
#django
from django.contrib import admin
#Models
from cride.circles.models import Circle
from cride.circles.models import Membership

@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
  """Circle Admin"""
  list_display =(
    'slug_name',
    'name',
    'is_public',
    'verified',
    'is_limited',
    'members_limit'
  )
  search_fields = ('slug_name', 'name')
  list_filter =(
    'is_public',
    'verified',
    'is_limited'
  )

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
  """Membership Admin"""