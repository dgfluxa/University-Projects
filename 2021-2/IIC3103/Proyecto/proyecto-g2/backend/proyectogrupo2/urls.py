from django.contrib import admin
from django.urls import path, include
from .router import router
from proyectogrupo2_api.Views.oc import OrdenCompraViewset, OrdenesCompraGeneralViewset
from proyectogrupo2_api.Views.stocks import StocksViewset, AlmacenesListViewset
from proyectogrupo2_api.Views.stocks import GeneralStocksViewset, OcsViewset, OCDetailViewset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('stocks/', StocksViewset.as_view(), name='stocks'),
    path('ordenes-compra/', OrdenesCompraGeneralViewset.as_view(), name='groupOCs'),
    path('ordenes-compra/<str:id>', OrdenCompraViewset.as_view(), name='oc'),
    path('almacenes/', AlmacenesListViewset.as_view(), name='almacenes'),
    path('generalStocks/', GeneralStocksViewset.as_view(), name='generalStocks'),
    path('ocs/', OcsViewset.as_view(), name='ocs'),
    path('oc_detail/<str:id>', OCDetailViewset.as_view(), name='oc_detail')
]