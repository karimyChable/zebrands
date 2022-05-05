# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from zebrands.products.models import Product
from zebrands.products.serializers import GetProductSerializer, PostProductSerializer
from zebrands.users.permissions import PermissionRequired


class ProductView(APIView):
    # model = Product
    # permission_classes = ((PermissionRequired),)

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product_serializer = GetProductSerializer(product)
            return Response(dict(success=True, data=product_serializer.data), status=status.HTTP_200_OK)
        except Exception as error:
            return Response(dict(success=False, error='Producto no encontrado'), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product_serializer = PostProductSerializer(product, data=request.data, partial=True)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return \
                    Response(
                        dict(
                            success=False,
                            errors=[x + "-" + y[0] for x, y in
                                    zip(product_serializer.errors.keys(),
                                        product_serializer.errors.values())]
                        ),
                        status=status.HTTP_400_BAD_REQUEST
                    )
        except Exception as error:
            return Response(dict(success=False, errors=['Ocurrio un error al editar el producto']),
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(dict(success=False, errors=['El producto no existe']),
                            status=status.HTTP_400_BAD_REQUEST)


class ProductListView(APIView):
    # model = Product
    # permission_classes = ((PermissionRequired),)

    def get(self, request):
        products = Product.objects.all()
        products_serializer = GetProductSerializer(products, many=True)
        return Response(dict(success=True, data=products_serializer.data, status=status.HTTP_200_OK))

    def post(self, request):
        try:
            product_serializer = PostProductSerializer(data=request.data, partial=True)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return \
                    Response(
                        dict(
                            success=False,
                            errors=[x + "-" + y[0] for x, y in
                                    zip(product_serializer.errors.keys(),
                                        product_serializer.errors.values())]
                        ),
                        status=status.HTTP_400_BAD_REQUEST
                    )
        except Exception as error:
            return Response(dict(success=False, errors=["Ocurrió un error al guardar el producto"]),
                        status=status.HTTP_400_BAD_REQUEST)
