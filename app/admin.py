from django.contrib import admin
from app.models import Concert
from app.models import Musician
from app.models import Ticket
from app.models import Order
from app.models import User

admin.site.register(Concert)
admin.site.register(Musician)
admin.site.register(Ticket)
admin.site.register(Order)
admin.site.register(User)
