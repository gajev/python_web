from django import forms
from django.forms import PasswordInput

from project_cars.cars.models import Profile, Car


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('profile_picture', 'first_name', 'last_name',)
        widgets = {
            "password": PasswordInput(
                attrs={'autocomplete': 'off', 'data-toggle': 'password'}),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class CarDeleteForm(CarEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
