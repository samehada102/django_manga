from django.apps import AppConfig


# class MangaappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'webapp'

# アプリケーション名の表示を変更
class SampleAppConfig(AppConfig):
    name = 'mangaapp'
    verbose_name = 'アプリ'
