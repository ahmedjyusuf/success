from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ZoomClassScheduleSerializer
from .models import ZoomClassSchedule

@api_view(['GET'])
def localized_zoom_time(request):
    user = request.user
    zoom_class_schedules = ZoomClassSchedule.objects.filter(student=user)
    serializer = ZoomClassScheduleSerializer(zoom_class_schedules, many=True, context={'request': request})
    return Response(serializer.data)