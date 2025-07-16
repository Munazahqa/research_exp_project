from django.urls import path                     
from . import views
urlpatterns = [
    path('api/experiments/submit', views.submit_to_mongo),
    path('api/researcher', views.mongo_postgres),
    path('api/experiments/<experiment_id>', views.retrieval_api),

]

