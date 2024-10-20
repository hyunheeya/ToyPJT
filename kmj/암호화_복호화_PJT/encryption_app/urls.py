from django.urls import path
from . import views

app_name="encryption_app"
urlpatterns = [
    path("",views.index, name='index'), # 메인 페이지
    path('encrypt/', views.encrypt, name='encrypt'),  # 암호화 페이지
    path('decrypt/', views.decrypt, name='decrypt'),  # 복호화 페이지
]