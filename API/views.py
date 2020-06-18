from .models import *
from .serializers import *
from .utils import send_mail


from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ShiftView(generics.ListCreateAPIView):
    queryset = ShiftInfo.objects.all()
    serializer_class = ShiftInfoSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data['shift_id'])
        shift_id = request.data['shift_id']
        emails = Register.objects.filter(
            shift_id=shift_id).values_list('email', flat=True)
        for email in emails:
            # print(email)
            send_mail(email, shift_id)

        return super().post(request, *args, **kwargs)


class PersonView(generics.ListCreateAPIView):
    queryset = PersonInfo.objects.all()
    serializer_class = PersonInfoSerializer


@api_view(['GET'])
def export(request, shift_id):
    people = Register.objects.filter(shift_id=shift_id)
    serializer = PersonInfoSerializer(people, many=True)
    return Response(serializer.data)
