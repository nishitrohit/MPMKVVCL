
from rest_framework import serializers
from .models import *

# first we define the serializers
class VendorRegistration_Serializer(serializers.ModelSerializer):
    class Meta:
        model = VendorRegistration
        fields = "__all__"

class Finance_Serializer(serializers.ModelSerializer):
    class Meta:
        model = finance_officer
        fields = "__all__"

class Working_Serializer(serializers.ModelSerializer):
    class Meta:
        model = working_officer
        fields = "__all__"


class NablRegistration_Serializer(serializers.ModelSerializer):
    class Meta:
        model = NablRegistration
        fields = "__all__"

