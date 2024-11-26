
import random


from django.core.cache import cache
from rest_framework.utils.serializer_helpers import ReturnDict

from  rest_framework.views import APIView
from  rest_framework import status
from  rest_framework.response import Response
from  rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

from sms_ir import SmsIr
from sms_cnfig import *

from users.admin import UserAdmin
from users.models import MyUser


sms_ir = SmsIr(
    api_key ,
    linenumber,
)

class RegisterView(APIView):
    def post(self,request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            user = MyUser.objects.get(phone_number=phone_number)
            return Response({'detail':'Phone number already registered'},status= status.HTTP_400_BAD_REQUEST)
        except MyUser.DoesNotExist:
            user = MyUser.objects.create(phone_number=phone_number , username= request.data('username'))
            """may error"""



        code = str(random.randint(1,9)) + str(random.randint(10,90))+str(random.randint(1,9))

        cache.set(str(phone_number) , code , 2*60+20)
        #send sms
        try:
            sms_ir.send_verify_code(
                number=phone_number,
                template_id=10000,
                parameters=[
                    {
                        "name": "code",
                        "value": code,
                    },
                ],
            )
        except Exception as e:
            return Response({'error':str(e)})

        return Response({"detail" : "code sent"})


class GetToken(APIView):
    def post(self, request):

        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        try:
            cashed_code= cache.get((str(phone_number)))
            if code == cashed_code:
               user =  MyUser.objects.get(phone_number=phone_number)
               user.verified = True
               refresh = RefreshToken.for_user(user.user)
               return Response({
                   'refresh': str(refresh),'access': str(refresh.access_token),}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid verification code."}, status=status.HTTP_400_BAD_REQUEST)
        except MyUser.DoesNotExist:
            return Response({"error": "Phone number not found."}, status=status.HTTP_404_NOT_FOUND)


# class TokenRefresh(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self,request):
#         phone_number = request.data.get('phone_number')
#         try:
#             user = MyUser.objects.get(phone_number=phone_number)
#         except MyUser.DoesNotExist:
#             return Response({'detail':'unregistered user'})
#
#         if user.verified:
#             refresh = RefreshToken.for_user(user.user)
#             return Response({
#                 'refresh': str(refresh), 'access': str(refresh.access_token), }, status=status.HTTP_200_OK)
#         else:
#             return Response({"detail": "unverified user"}, status=status.HTTP_400_BAD_REQUEST)







