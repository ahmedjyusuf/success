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

    def get_next_class_time(user):
        user_obj = User.objects.get(username=user)
        user_timezone = user_obj.timezone
        print('\n\n\n',user_timezone)
        current_time = timezone.now().astimezone(pytz.timezone(user_timezone))
        
        next_class_time = ZoomClassSchedule.objects.filter(student=user_obj, class_time__gt=current_time).order_by('class_time').first()
        
        if next_class_time:
            return next_class_time.class_time.astimezone(pytz.timezone(user_timezone))
        else:
            return None

    # Usage
    # next_class_time = get_next_class_time('nasir')
    # if next_class_time:
    #     print(f"Next class time for 'nasir' in the user's timezone: {next_class_time}")
    # else:
    #     print("No upcoming class found for 'nasir'")

    from datetime import date, timedelta
    from django.contrib.auth import get_user_model
    from django.utils import timezone

    # def get_schedule_for_month():
    #     current_date = timezone.now().date()
    #     year = current_date.year
    #     month = current_date.month

    #     start_date = date(year, month, 1)
    #     end_date = start_date.replace(day=28) + timedelta(days=4)
    #     end_date = min(end_date, date(year, month, 31))

    #     zoom_class_schedules = ZoomClassSchedule.objects.filter(class_time__year=year, class_time__month=month, repeat=True)

    #     for zoom_class_schedule in zoom_class_schedules:
    #         days_of_week = zoom_class_schedule.days_of_week.all()
    #         print(f"ZoomClassSchedule: {zoom_class_schedule}, Days of Week: {days_of_week}")
    #     get_schedule_for_month()

    def get_schedule_for_month2():
        print('hi\n\n')
        current_date = timezone.now().date()
        year = current_date.year
        month = current_date.month

        start_date = date(year, month, 1)
        end_date = start_date.replace(day=28) + timedelta(days=4)
        end_date = min(end_date, date(year, month, 31))

        user = User.objects.get(username='nasir')
        user_timezone = ZoneInfo(user.timezone)

        today_weekday = current_date.weekday()
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        days_of_week = DayOfWeek.objects.filter(name__in=day_names[today_weekday:])

        zoom_class_schedules = ZoomClassSchedule.objects.filter(
            class_time__year=year,
            class_time__month=month,
            repeat=True,
            days_of_week__in=days_of_week
        )

        for zoom_class_schedule in zoom_class_schedules:
            class_time = zoom_class_schedule.class_time.astimezone(user_timezone)
            days_of_week = zoom_class_schedule.days_of_week.all()
            print(f"ZoomClassSchedule: {zoom_class_schedule}, Class Time (User's Timezone): {class_time}, Days of Week: {days_of_week}")
    # print(get_schedule_for_month2())
    from django.core.mail import send_mail

    def send_email():
        subject = 'Test Email'
        message = 'This is a test email from Django.'
        # from_email = 'devauth213@gmail.com'
        from_email = 'info@metatutoring.us'
        recipient_list = ['dfm880@gmail.com']

        send_mail(subject, message, from_email, recipient_list)
        return 'Email sent successfully'
    # send_email()

    def evc(props):
        print(props.get('user'))
        # if not props:
        #     return 'you have to provide an object props'
    evc(props={'user':'hey'})




