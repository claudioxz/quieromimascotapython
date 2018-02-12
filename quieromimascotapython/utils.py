
from rest_framework import status, generics
from rest_framework.response import Response


class ListCreateRelation(generics.GenericAPIView):
    """
    Esta clase sirve para resolver end_points del tipo documento/1/articulos, por ejemplo.
    La clase acepta 2 tipos de metodos http: GET y POST.
    GET: Segun el end_point mencionado anteriormente, retornaria una lista de
         articulos asociado con el documento con pk=1
    POST: Segun el end_point mencionado anteriormente, crearia un
         nuevo elemento articulo relacionado con el documento con pk=1
    related_queryset_name: Seria el related_name que esta en el modelo al crear la ForeignKey.
    Debe ser sobre escrito, de tipo String.
    related_model_name: Seria el nombre del modelo relacionado, por ejemplo, en el ejemplo anterior mencionado
                       es 'documento'. De tipo String, debe ser sobre escrito.
    related_model_class: Seria la clase del modelo relacionado, por ejemplo, en el ejemplo anterior mencionado
                       es Documento, de tipo Class de algun modelo, debe ser sobre escrito.
    serializer_class: Clase serializer del objeto a enlistar o crear, ArticuloSerializer para el ejemplo anteriormente
                      mencionado.
    """
    http_method_names = [u'get', u'post']
    related_queryset_name = None
    related_model_name = None
    related_model_class = None

    def get_queryset(self):
        pass

    def get(self, request, pk):
        parent_instance = self.get_parent_instance(pk)
        if parent_instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset = getattr(parent_instance, self.related_queryset_name)
        instances = queryset.all()
        serializer = self.get_serializer(instances, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, pk):
        parent_instance = self.get_parent_instance(pk)

        if parent_instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data.update({self.related_model_name: pk})
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get_parent_instance(self, pk):
        ParentModelClass = self.related_model_class
        try:
            instance = ParentModelClass.objects.get(pk=pk)
            return instance
        except ParentModelClass.DoesNotExist:
            return None