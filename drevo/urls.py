from django.urls import path
from .views import DrevoListView, DrevoView, ZnanieDetailView, ZnanieByLabelView

urlpatterns = [
    path('category/<int:pk>', DrevoListView.as_view(), name = 'drevo_type'),
    path('drevo/', DrevoView.as_view(), name = 'drevo'),
    path('znanie/<int:pk>', ZnanieDetailView.as_view(), name = 'zdetail'),
    path('label/<int:pk>', ZnanieByLabelView.as_view(), name = 'zlabel'),
]