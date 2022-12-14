from django.urls import path, include
from . import views


app_name = "articles"


urlpatterns = [
    # 메인 페이지
    path("", views.main, name="main"),
    # 모든 키보드 다 보여주는 페이지
    path("all/", views.all, name="all"),
    path("scroll_data/", views.scroll_data, name="scroll_data"),
    path("<int:pk>/detail/", views.detail, name="detail"),
]
