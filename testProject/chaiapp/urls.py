
from django.urls import path
from .views import all_chai, chai_detail, chai_store_view

urlpatterns = [
    path('', all_chai.as_view(), name="all_chai"),
    path('<int:chai_id>/',chai_detail.as_view(), name="chai_detail"),
    path('chai_stores/',chai_store_view.as_view(), name="chai_store_view")
]
