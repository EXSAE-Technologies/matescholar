from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, "users")
router.register(r'school', views.SchoolViewSet, "school")
router.register(r'program', views.ProgramViewSet, "program")
router.register(r'course', views.CourseViewSet, "course")

urlpatterns = router.urls