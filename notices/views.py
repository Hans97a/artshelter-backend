from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from django.core.paginator import Paginator
from django.db.models import Q


class NoticeListView(APIView):
    def get(self, request):
        q = request.GET.get("q", None)
        pinned_notices = models.Notice.objects.filter(is_pinned=True).order_by(
            "-created_at"
        )
        if q == "":
            notices = models.Notice.objects.filter(is_pinned=False).order_by(
                "-created_at"
            )

        else:
            notices = models.Notice.objects.filter(
                Q(title__icontains=q) | Q(content__icontains=q)
            ).order_by("-created_at")
        if not notices:
            if pinned_notices:
                pinned_serializer = serializers.NoticeSerializer(
                    pinned_notices, many=True
                )
                return Response(
                    {"ok": True, "pinned": pinned_serializer.data},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"ok": False, "detail": "결과가 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        page = request.query_params.get("page", 1)
        page_size = request.query_params.get("page_size", 10)
        try:
            paginator = Paginator(notices, page_size)
            result = paginator.page(page)
            serializer = serializers.NoticeSerializer(
                result,
                many=True,
            )
            pinned_serializer = serializers.NoticeSerializer(pinned_notices, many=True)

            return Response(
                {
                    "ok": True,
                    "count": notices.count(),
                    "pinned": pinned_serializer.data,
                    "results": serializer.data,
                    "next": result.has_next(),
                    "prev": result.has_previous(),
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {"ok": False, "detail": "존재하지 않는 페이지입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class NoticeDetailView(APIView):
    def get(self, request, pk):
        try:
            notice = models.Notice.objects.get(pk=pk)
        except Exception:
            return Response(
                {"ok": False, "detail": "존재하지 않는 게시물입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        prev_notice = models.Notice.objects.filter(pk__lt=pk, is_pinned=False).last()
        next_notice = models.Notice.objects.filter(pk__gt=pk, is_pinned=False).first()
        notice.visited += 1
        notice.save()
        serializer = serializers.NoticeSerializer(notice)
        return Response(
            {
                "result": serializer.data,
                "next": {"title": next_notice.title, "pk": next_notice.pk}
                if next_notice
                else False,
                "prev": {"title": prev_notice.title, "pk": prev_notice.pk}
                if prev_notice
                else False,
            },
            status=status.HTTP_200_OK,
        )
