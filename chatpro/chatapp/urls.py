from . import views
from django.urls import path

urlpatterns=[

   path('chatt/', views.chatbot_view, name='chatbot_view'),
]

