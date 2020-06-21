from .models import PersonInfo,ShiftInfo,Register
from rest_framework import serializers


class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','phone_number','name','email')
        model = PersonInfo

class ShiftInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('shift_id','start','end','empty_ticket','risk_level','time')
        model = ShiftInfo

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('rid','shift_id','email')
        model = Register