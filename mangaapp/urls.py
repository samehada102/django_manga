from django.urls import path

# views.pyで定義した画面を読み込み
from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, RankingView

# 各画面のurlを設定
urlpatterns = [
    # 検索一覧画面
    path('',  ItemFilterView.as_view(), name='index'),
    # 詳細画面
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    # 登録画面
    path('create/', ItemCreateView.as_view(), name='create'),
    # 更新画面
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    # 削除画面
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    # ランキング画面
    path('ranking/', RankingView.as_view(), name='ranking'),
]