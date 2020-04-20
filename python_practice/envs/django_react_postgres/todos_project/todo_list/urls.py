from rest_framework import routers

from .views import TodoView

router = routers.DefaultRouter()
router.register('todos', TodoView, 'todos')
# router.register('<URL prefix>', '<view class>', '<URL name>')

urlpatterns = router.urls