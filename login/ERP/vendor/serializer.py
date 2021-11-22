
from rest_framework import serializers
from .models import *

# first we define the serializers
class VendorRegistration_Serializer(serializers.ModelSerializer):
    class Meta:
        model = VendorRegistration
        fields = "__all__"





