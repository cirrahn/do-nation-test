from django.urls import path

from . import views

urlpatterns = [
    path("", views.detail, name="detail-current-user"),
    path("<int:user_id>/", views.detail, name="detail"),
]
