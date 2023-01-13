from django.contrib import admin
from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter



router=DefaultRouter()
router.register('api/travel',views.Travelviewset)
router.register('api/testimonialsData',views.TestimonialsDataviewset)
router.register('api/frequentlyAskedDatas',views.FrequentlyAskedDatasviewset)
router.register('api/postDatas',views.PostDatasviewset)
router.register('api/teamsdata',views.Teamsdataviewset)
router.register('api/featuredServicwesDatas',views.FeaturedServicwesDatasviewset)




urlpatterns = [
      path('',include(router.urls)),
]
