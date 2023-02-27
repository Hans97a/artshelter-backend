from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class QuestionView(APIView):
    def post(self, request):
        serializer = serializers.QuestionSerializer(data=request.data)
        print(" ㅋㅋ", request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                # serializer = serializers.QuestionSerializer(serializer)
                return Response(
                    {"ok": True, "detail": "저장 완료"},
                    status=status.HTTP_201_CREATED,
                )
            except Exception:
                print("안되네")
                return Response("ㅋㅋ")
        else:
            return Response(serializer.errors)
