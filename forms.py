from django import forms
from .models import Upimage
#画像アップロードフォーム
class UpimageForm(forms.ModelForm):
    class Meta:
        model = Upimage
        fields = ('img', )