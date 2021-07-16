from rest_framework.response import Response
from rest_framework.views import APIView

from .models import StudentModel
from .serializer import StudentSerializer

class AllStudent(APIView):

    def get(self, request):

        student_model = StudentModel.objects.all()
        student_serializer = StudentSerializer(student_model, many=True)
        return Response(student_serializer.data)

class AddStudent(APIView):

    def post(self, request):

        data = {

            'name' : request.data.get('name'),
            'age' :request.data.get('age')

        }

        student_serializer = StudentSerializer(data=data)

        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        else:
            return Response(student_serializer.errors)

class SpecifStudent(APIView):

    def get_student(self, id):
        try:
            return StudentModel.objects.get(id=id)
        except StudentModel.DoesNotExist:
            return Response('I did not find out!')

    def get(self, request, id):

        student = self.get_student(id)
        student_serializer = StudentSerializer(student)
        try:
            return Response(student_serializer.data)
        except StudentModel.objects.DoesNotExist:
            return Response('Try again, bitch!')
    
    def delete(self, request, id):

        student = self.get_student(id)
        student.delete()
        return Response('Done, baby!')