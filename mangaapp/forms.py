from django import forms
from .models import Item

# 登録画面、更新画面フォームの定義
class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        # 作品名、読み終えた巻、最新巻、次巻発売日、備考欄　を入力フォームとして設定
        fields = ('name','finish','newest','next','memo')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'記入例：ONE PIECE'}),
                    'finish': forms.NumberInput(attrs={'min':1}),
                    'newest': forms.NumberInput(attrs={'min':1}),
                    'next': forms.DateInput(attrs={'type':'date'}),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }