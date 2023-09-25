from rest_framework import routers
from . import views
router =routers.SimpleRouter()
router.register('product',views.ProductViewset)
router.register('detail',views.ProductDetailViewset)
router.register('side',views.SideViewset)
router.register('movment',views.MovmentViewset)
urlpatterns = router.urls