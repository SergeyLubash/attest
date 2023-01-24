from django.urls import path

from . import views

urlpatterns = [
    path('subject_net/create', views.Subject_netCreateView.as_view()),
    path('subject_net/list', views.Subject_netListView.as_view()),
    path('subject_net/<pk>', views.Subject_netView.as_view()),
    path('product/create', views.ProductCreateView.as_view()),
    path('product/list', views.ProductListView.as_view()),
    path('product/<pk>', views.ProductView.as_view()),
    path('contact/create', views.ContactCreateView.as_view()),
    path('contact/list', views.ContactListView.as_view()),
    path('contact/<pk>', views.ContactView.as_view()),

]
