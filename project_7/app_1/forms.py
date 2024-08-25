from django import forms


class UpdateForm(forms.Form):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'col': 12, 'rows': 3}),
        label='Описание'
    )
    price = forms.IntegerField(label='Цена')
