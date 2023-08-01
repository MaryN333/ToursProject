from tastypie.resources import ModelResource
from shop.models import Category, Tour
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


# Create your models here.

# эти модели наз. ресурсами


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']  # jen cteni


class TourResource(ModelResource):
    class Meta:
        queryset = Tour.objects.all()
        resource_name = 'tours'
        allowed_methods = ['get', 'post', 'delete']
        # #301 чтобы в postman не отображ
        # excludes = ['reviews_qty', 'created_at']
        excludes = ['created_at']
        # # lekce 295 dobavili
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    # pridame category_id pro POST method (API), aby mohli pridat tour a uvest category_id
    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle

    # def dehydrate_title(self, bundle):
    #     return bundle.data['title'].upper()
