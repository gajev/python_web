from django import forms
from django.forms import PasswordInput

from final.fruits.models import Profile, Fruit


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('image_url', 'age',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password', 'autocomplete': 'off', 'data-toggle': 'password'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description'
                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(),
            'image_url': forms.URLInput(),
            'description': forms.Textarea(),
            'nutrition': forms.Textarea()

        }


class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('nutrition',)
        widgets = {
            'name': forms.TextInput(),
            'image_url': forms.URLInput(),
            'description': forms.Textarea(),
        }
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


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('email', 'password',)
