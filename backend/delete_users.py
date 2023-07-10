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

    user_obj = User.objects.all()
    for user in user_obj:
        if not user.is_staff:
            print(user)
            user.delete()
    print(user_obj)
        