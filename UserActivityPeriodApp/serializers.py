from rest_framework import serializers
from . models import *

class ActivityPeriodSerializer(serializers.ModelSerializer):

    # members = UserSerializer(read_only=True)

    class Meta:
        model = ActivityPeriods
        fields = ('start_date','end_date')

class UserSerializer(serializers.ModelSerializer):
    tz = serializers.CharField()
    activity_periods = ActivityPeriodSerializer(read_only=True, many=True)

    class Meta:
        model = Users
        fields = ('id', 'real_name','tz','activity_periods') 

