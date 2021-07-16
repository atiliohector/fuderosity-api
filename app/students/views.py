from rest_framework.response import Response
from rest_framework.views import APIView

from .models import StudentModel
from .serializer import StudentSerializer

class AllStudent(APIView):

    def get(self, request):

        student_model = StudentModel.objects.all()
        student_serializer = StudentSerializer(student_model, many=True)
        return Response(student_serializer.data)