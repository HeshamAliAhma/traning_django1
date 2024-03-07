from django.urls import path
from . import views


app_name = 'post'


urlpatterns = [
    path('', views.AllPost , name='post_details'),
    path('<int:id>/', views.PostDetail , name='post_details' ),

]
