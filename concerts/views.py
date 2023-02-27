from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from django.core.paginator import Paginator
from django.db.models import Q


class ConcertListView(APIView):
    def get(self, request):
        concerts = models.Concert.objects.all().order_by("-date")
        page = request.query_params.get("page", 1)
        page_size = request.query_params.get("page_size", 1)
        try:
            paginator = Paginator(concerts, page_size)
            result = paginator.page(page)
            serializer = serializers.ConcertSerializer(
                result, many=True, context={"request": request}
            )
            return Response(
                {
                    "count": concerts.count(),
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


class ConcertDetailView(APIView):
    def get(self, request, pk):
        # 이전과 다음 게시물 보여주기  lt gt으로 비교해서 순서로 필터링하고 first하면 될듯
        try:
            concert = models.Concert.objects.get(pk=pk)
        except Exception:
            return Response(
                {"ok": False, "detail": "존재하지 않는 게시물입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = serializers.ConcertSerializer(
            concert, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class ConcertBannerView(APIView):
    def get(self, request):
        concerts = models.Concert.objects.filter(is_banner=True).order_by("-date")
        if concerts:
            serializer = serializers.ConcertSerializer(
                concerts, many=True, context={"request": request}
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"ok": False, "detail": "배너가 없습니다."}, status=status.HTTP_400_BAD_REQUEST
            )
