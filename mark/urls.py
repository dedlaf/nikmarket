from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('auth', views.auth),
    path('register', views.register),
    path('profile', views.profile),
    path('profile-admin', views.profile_admin),
    path('logout', views.logouting),
    path('cart', views.cart),
    path('add_to_cart/<int:product_id>/', views.add_to_cart,name='add_to_cart'),
    path('min_to_cart/<int:product_id>/', views.min_to_cart, name='min_to_cart'),
    path('task', views.task)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)