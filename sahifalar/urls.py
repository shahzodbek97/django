from django.urls import path
from .views import HomePageView,AboutePageView,ContactPageView,ProductPageView

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutePageView.as_view(),name='about'),
    path('product/',ProductPageView.as_view(),name='product'),
    path('contact/',ContactPageView.as_view(),name='contact'),
]