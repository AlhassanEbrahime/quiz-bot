from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import RandomQuestionSerializer


class RandomQuestionView(APIView):
    
    def get(self, request, format= None, **Kwargs):
        question = Question.objects.filter().order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)