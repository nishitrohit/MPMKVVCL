
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

class Officer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = officer
        fields = "__all__"


class Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = my_order
        fields = "__all__"

class Dispatch_Serializer(serializers.ModelSerializer):
    class Meta:
        model = dispatch
        fields = "__all__"


class Tkclogin_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TkcLogin
        fields = "__all__"


