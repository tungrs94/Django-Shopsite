from django.urls import path
from .views import HomeView, BlogView, ContactView, ProductView

urlpatterns = [
    path('', HomeView.as_view(), name = 'index'),
    path('blog/', BlogView.as_view(), name = 'blog'),
    # path('cart/', CartView.as_view(), name = 'cart'),  (nên tạo url cart bên app core hay app cart)
    path('contact/', ContactView.as_view(), name = 'contact'),
    path('product/', ProductView.as_view(), name = 'product'),
]
