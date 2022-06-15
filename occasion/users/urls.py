from users import views
from django.urls import path


urlpatterns = [
    path('create/', views.UserCreateApiView.as_view()),
]
