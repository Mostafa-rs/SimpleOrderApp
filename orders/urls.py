from django.urls import path

# Local
from orders import apis

urlpatterns = [
    path('', apis.OrderRetrieveListCreateAPI.as_view()),
    path('<int:pk>/', apis.OrderRetrieveListCreateAPI.as_view()),
]

