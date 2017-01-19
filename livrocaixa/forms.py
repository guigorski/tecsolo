from django import forms

from .models import Gasto
from .models import Amostra

class AddForm(forms.ModelForm):

    class Meta:
        model = Amostra
        fields = ('Cliente', 'Cod_Amostra', 'Valor', 'Propriedade','Gleba', 'Municipio', 'Amostras', 'Pago',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Gasto
        fields = ('Nome','Valor',)
