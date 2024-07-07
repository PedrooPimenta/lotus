from rest_framework.routers import DefaultRouter
from api.views import PerfilViewSet, UserHasPerfilViewSet,ProductViewSet, UserViewSet, SuitsViewSet, PantsViewSet,WomenSuitViewSet,AccessoriesViewSet,UserHasSuitsViewSet,SalesViewSet, DataDashViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)

router.register(r'perfil', PerfilViewSet, basename='perfil')

router.register(r'userhasperfil', UserHasPerfilViewSet, basename='userhasperfil')

router.register(r'product', ProductViewSet, basename='product')
router.register(r'user', UserViewSet, basename='user')

router.register(r'suits', SuitsViewSet, basename='suits')

router.register(r'pants', PantsViewSet, basename='pants')

router.register(r'womensuit', WomenSuitViewSet, basename='womensuit')

router.register(r'accessories', AccessoriesViewSet, basename='accessories')

router.register(r'userhassuits', UserHasSuitsViewSet, basename='userhassuits')

router.register(r'sales', SalesViewSet, basename='sales')

router.register(r'datadash', DataDashViewSet, basename='datadash')


urlpatterns = router.urls