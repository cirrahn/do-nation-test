from django.contrib import admin

from .models import ActionType, VegOutAction, CleanYourBillsActions

admin.site.register(ActionType)
admin.site.register(VegOutAction)
admin.site.register(CleanYourBillsActions)
