from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from dealer_app.forms import CustomDealerCreationForm,CustomDealerChangeForm
from dealer_app.models import Dealer

class CustomUserAdmin(UserAdmin):
    add_form=CustomDealerCreationForm
    form=CustomDealerChangeForm
    list_display=['email','username','is_staff','is_superuser']
    



admin.site.register(Dealer,CustomUserAdmin)

