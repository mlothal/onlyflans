from django.contrib import admin
from .models import Flan, ContactForm

# Registra el modelo Flan
admin.site.register(Flan)

# Registra el modelo ContactForm
admin.site.register(ContactForm)
