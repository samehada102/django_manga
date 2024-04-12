from django.db import models
from django.core import validators

# Create your models here.

# クラスを定義
class Item(models.Model):

    # 作品名
    name = models.CharField(
        verbose_name='作品名',
        max_length=200, # 最大文字数を設定
    )

    # 読み終えた巻
    finish = models.IntegerField(
        verbose_name='読み終えた巻',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )

    # 最新巻
    newest = models.IntegerField(
        verbose_name='最新巻',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )

    # 次巻発売日
    next = models.DateField(
        verbose_name='次巻発売日',
        blank=True,
        null=True,
    )

    # 備考欄
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )

    # 登録日
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True, # データ追加時に現在時間を設定する
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'