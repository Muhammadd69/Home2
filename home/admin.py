from django.contrib import admin
from .models import Home, Customer, Agent, Contact


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('price', 'city', 'location')
    list_filter = ('price', 'city', 'location')
    search_fields = ('price', 'city', 'location')
    ordering = ('price',)
    list_display_links = ('price',)

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')
    list_filter = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')