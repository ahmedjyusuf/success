from rest_framework import serializers
from .models import ZoomClassSchedule, ZoomClass
import pytz

class ZoomClassSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()
    class Meta:
        model = ZoomClass
        fields = '__all__' #['id', 'link', 'name', 'teacher']


class ZoomClassScheduleSerializer(serializers.ModelSerializer):
    days_of_week = serializers.StringRelatedField(many=True)
    zoom_class = ZoomClassSerializer()

    class Meta:
        model = ZoomClassSchedule
        fields = ['id', 'zoom_class', 'class_time', 'days_of_week', 'repeat']

    def to_representation(self, instance):
        # Convert class_time to user's local timezone
        user = self.context['request'].user
        user_tz = pytz.timezone(user.timezone)
        instance.class_time = instance.class_time.astimezone(user_tz)
        return super().to_representation(instance)
