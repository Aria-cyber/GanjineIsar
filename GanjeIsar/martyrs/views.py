



from rest_framework.views import APIView

from  rest_framework.response import Response

from .models import Martyr
from .serializers import  MartyrSerializer

class MartyrView(APIView):
    def get(self, request):
        martyrlist = Martyr.objects.all()
        serializer = MartyrSerializer(martyrlist, many=True)
        return Response(serializer.data)

