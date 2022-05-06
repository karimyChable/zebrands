# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from zebrands.logs.models import Log
from zebrands.logs.serializers import GetLogSerializer, PostLogSerializer
from zebrands.users.permissions import PermissionRequired


class LogView(APIView):
    model = Log
    permission_classes = [PermissionRequired]

    def get(self, request, pk):
        try:
            log = Log.objects.get(pk=pk)
            log_serializer = GetLogSerializer(log)
            return Response(dict(success=True, data=log_serializer.data), status=status.HTTP_200_OK)
        except Exception:
            return Response(dict(success=False, error='Log no encontrado'), status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        try:
            log = Log.objects.get(pk=pk)
            log_serializer = PostLogSerializer(log, data=request.data, partial=True)
            if log_serializer.is_valid():
                log_serializer.save()
                return Response(log_serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return \
                    Response(
                        dict(
                            success=False,
                            errors=[x + "-" + y[0] for x, y in
                                    zip(log_serializer.errors.keys(),
                                        log_serializer.errors.values())]
                        ),
                        status=status.HTTP_400_BAD_REQUEST
                    )
        except Exception as error:
            return Response(dict(success=False, errors=['Ocurrio un error al editar el log']),
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            log = Log.objects.get(pk=pk)
            log.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(dict(success=False, errors=['El log no existe']),
                            status=status.HTTP_400_BAD_REQUEST)


class LogListView(APIView):
    model = Log
    permission_classes = [PermissionRequired]

    def get(self, request):
        logs = Log.objects.all()
        logs_serializers = GetLogSerializer(logs, many=True)
        return Response(dict(success=True, data=logs_serializers.data, status=status.HTTP_200_OK))

    def post(self, request):
        try:
            log_serializer = PostLogSerializer(data=request.data, partial=True)
            if log_serializer.is_valid():
                log_serializer.save()
                return Response(log_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return \
                    Response(
                        dict(
                            success=False,
                            errors=[x + "-" + y[0] for x, y in
                                    zip(log_serializer.errors.keys(),
                                        log_serializer.errors.values())]
                        ),
                        status=status.HTTP_400_BAD_REQUEST
                    )
        except Exception as error:
            return Response(dict(success=False, errors=["Ocurrió un error al guardar el log"]),
                        status=status.HTTP_400_BAD_REQUEST)
