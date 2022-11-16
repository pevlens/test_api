from django.urls import path, re_path, include
from .views import CategoryViewSets, TransactionViewSets, BalanseUser
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSets, basename="category")
router2 = routers.SimpleRouter()
router2.register(r'transactions', TransactionViewSets, basename="transactions")

urlpatterns = [
    path("api/" , include(router.urls)),
    path("api/" , include(router2.urls)),
    path("api/balance/" , BalanseUser.as_view(), name='balance'),
    path("api/auth/", include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
    