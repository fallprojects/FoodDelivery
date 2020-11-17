from django.forms import ModelForm
from .models import Complect



class ComplectForm(ModelForm):
    class Meta:
        model = Complect
        fields = '__all__'
        exclude = ['sale','price']