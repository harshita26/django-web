from django.urls import path
from . import views
urlpatterns = [
    path('',views.index ),
    path('destination',views.dest ),
    path('details',views.details ),
]