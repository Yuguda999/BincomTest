from django.forms import ModelForm
from .models import AnnouncedPuResults


class PollingUnitForm(ModelForm):
    class Meta:
        model = AnnouncedPuResults
        fields = '__all__'
