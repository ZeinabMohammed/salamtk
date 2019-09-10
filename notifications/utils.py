from .serializers import NotificationSerializer

def push_notifications(user,title,body):
    data = {

        'user': user,
        'title': title,
        'body': body
    }

    serializer = NotificationSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=user)
    devices = FCMDevice.objects.filter(user=user)
    devices.send_message(title='hi', body='hello')

# def push_notifications(doctor,title,body):
#     data = {
#         'doctor': doctor,
#         'title': title,
#         'body': body
#     }
#     serializer = CommentNotficationSerializer(data=data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(doctor=doctor)
#         devices = FCMDevice.objects.filter(doctor=doctor)
#         devices.send_message(title='hi', body='hello')