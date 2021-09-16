from django.urls import path
from .views import VscwebList, VscwebDetail

urlpatterns = [
    path('list/', VscwebList.as_view(), name='list'),
    path('detail/<int:pk>/', VscwebDetail.as_view(), name='detail'),
]
