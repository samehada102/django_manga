from django_filters import filters
from django_filters import FilterSet
# models.pyを読み込み
from .models import Item

class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'

class ItemFilter(FilterSet):

    # 作品名と備考を部分一致に変更
    name = filters.CharFilter(label='作品名', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
        ),
        field_labels={
            'name': '作品名',
        },
        label='並び順'
    )

    class Meta:
        model = Item
        fields = ('name', 'memo',)