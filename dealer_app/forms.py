from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from dealer_app.models import Dealer

class CustomDealerCreationForm(UserCreationForm):
    class Meta:
        model=Dealer
        fields=['username','email']



class CustomDealerChangeForm(UserChangeForm):
    class Meta:
        model=Dealer
        fields=['username','email']