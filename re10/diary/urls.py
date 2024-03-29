from django.urls import path, include
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('intro/', views.IntroView.as_view(), name='intro')
]
