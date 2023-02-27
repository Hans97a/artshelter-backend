from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from django.core.paginator import Paginator


class EducationListView(APIView):
    def get(self, request):
        edus = models.Education.objects.all().order_by("-created_at")
        page = request.query_params.get("page", 1)
        page_size = request.query_params.get("page_size", 12)
        try:
            paginator = Paginator(edus, page_size)
            result = paginator.page(page)
            serializer = serializers.EducationSerializer(
                result, many=True, context={"request": request}
            )

            return Response(
                {
                    "count": edus.count(),
                    "results": serializer.data,
                    "next": result.has_next(),
                    "prev": result.has_previous(),
                },
                status=status.HTTP_200_OK,
            )
        except Exception:
            return Response(
                {"ok": False, "detail": "존재하지 않는 페이지입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class EducationDetailView(APIView):
    def get(self, request, pk):
        try:
            edu = models.Education.objects.get(pk=pk)
        except Exception:
            return Response(
                {"ok": False, "detail": "존재하지 않는 게시물입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = serializers.EducationSerializer(edu)
        return Response(serializer.data, status=status.HTTP_200_OK)
