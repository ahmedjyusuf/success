from manage import main

if __name__ == '__main__':  
    main()
    from users.models import User
    import pytz

    from django.contrib.auth import get_user_model
    from django.utils import timezone
    from zoom.models import ZoomClass, ZoomClassSchedule, DayOfWeek 
    from zoneinfo import ZoneInfo
    User = get_user_model()
    user = User.objects.first()
    print(user)
    from django.utils import timezone
    # user = User.objects.first()
    from zoneinfo import ZoneInfo
    from django.utils import timezone

    import pytz
    from django.utils import timezone

    def zoom():
        user = User.objects.first()
        user_timezone = user.timezone

        # Query ZoomClassSchedule model for schedules belonging to the user
        zoom_class_schedules = ZoomClassSchedule.objects.filter(student=user)

        # Convert class times to user's local timezone
        user_tz = pytz.timezone(user.timezone)
        for schedule in zoom_class_schedules:
            schedule.class_time = schedule.class_time.astimezone(user_tz)
            print(schedule.class_time)
        return zoom_class_schedules


    zoom()



   
