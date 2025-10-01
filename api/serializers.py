from .models import Listing, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):
    # deeph = §1
    # category = CategorySerializer()
    class Meta:
        model = Listing
        fields = '__all__'
        depth = 1
        # extra_kwargs = {
        #     'price' : {'min_value': 1}
        # }   