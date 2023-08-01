from django.urls import path, include
from api.models import TourResource, CategoryResource
from tastypie.api import Api

api = Api(api_name='v1')
tour_resource = TourResource()
category_resource = CategoryResource()
api.register(tour_resource)
api.register(category_resource)


# api/v1/tours/         GET, POST
# api/v1/tours/1/       GET, DELETE
# api/v1/categories/    GET
# api/v1/categories/1/


urlpatterns = [
    path('', include(api.urls), name='index')
]
