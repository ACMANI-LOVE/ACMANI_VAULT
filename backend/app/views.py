
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from .models import *
from .serializers import *

# =========+=========+=========+=========+=========+
# ViewSets
# =========+=========+=========+=========+=========+

class ConfigsViewSet(viewsets.ModelViewSet):
  queryset = Constants.objects.all() # FIX Model
  serializer_class  = ConstantsSerializer # FIX Serializer
  def list(self):
    constants = Constants.objects.all()
    phrases   = Phrases.objects.order_by("id").first()
    weights   = Weights.objects.order_by("id").first()
    constants_data = ConstantsSerializer(constants, many=True)
    phrases_data   = PhrasesSerializer(phrases)
    weights_data   = WeightsSerializer(weights)
    data = {
      "Constants":constants_data.data,
      "Phrases":  phrases_data,
      "Weights":  weights_data
    }
    return Response({ data }, status=status.HTTP_200_OK)

  def update(self, request):
    req_data = request.data
    try:
      tgt_id = req_data.get("id")
      tgt_phrases = Phrases.objects.get(pk=tgt_id)
      tgt_weights = Weights.objects.get(pk=tgt_id)
    except Phrases.DoesNotExist | Weights.DoesNotExist:
      return Response({"message":"Models Does not Found."}, status=status.HTTP_404_NOT_FOUND)

    phrases = req_data.get("Phrases",{})
    weights = req_data.get("Weights",{})

    phrases_serializer = PhrasesSerializer(tgt_phrases, data=phrases, partial=False)
    weights_serializer = WeightsSerializer(tgt_weights, data=weights, partial=False)
    if phrases_serializer.is_valid() & weights_serializer.is_valid():
      phrases_serializer.save()
      weights_serializer.save()
      return Response({"message":"Update Success."}, status=status.HTTP_200_OK)

    return Response({"message":"Update Failed."}, status=status.HTTP_400_BAD_REQUEST)

  def create(self, request, *args, **kwargs):
    req_data = request.data
    # Transaction Start
    with transaction.atomic():
      if "create" in req_data:
        for item in req_data.get("create",[]):
          serializer = ConstantsSerializer(data=item)
          if serializer.is_valid():
            serializer.save()
          else:
            return Response({"message":"Add Failed."}, status=status.HTTP_400_BAD_REQUEST)

      if "update" in req_data:
        for item in req_data.get("update",[]):
          try:
            tgt_id = item.get("id")
            target = Constants.objects.get(pk=tgt_id)
            serializer = ConstantsSerializer(target, data=item, partial=True)
            if serializer.is_valid():
              serializer.save()
            else:
              return Response({"message":"Update Failed."}, status=status.HTTP_400_BAD_REQUEST)
          except Constants.DoesNotExist:
             return Response({"message":"Models Does not Found."}, status=status.HTTP_404_NOT_FOUND)

      if "delete" in req_data:
        for item in req_data.get("delete",[]):
          try:
            tgt_id = item.get("id")
            target = Constants.objects.get(pk=tgt_id)
            target.delete()
          except Constants.DoesNotExist:
             return Response({"message":"Models Does not Found."}, status=status.HTTP_404_NOT_FOUND)

      return Response({"message":"Update Success."}, status=status.HTTP_200_OK)
# =========+=========+=========+=========+=========+

class GroupsViewSet(viewsets.ModelViewSet):
  queryset = Groups.objects.all() # FIX Model
  serializer_class  = GroupsSerializer # FIX Serializer
  def list(self, request, *args, **kwargs):
    print("CALL LIST(GET)")
    return super().list(request, *args, **kwargs)
  def create(self, request, *args, **kwargs):
    print("CALL CREATE(POST)")
    return super().create(request, *args, **kwargs)
  def partial_update(self, request, *args, **kwargs):
    print("CALL PART UPD(PATCH)")
    return super().partial_update(request, *args, **kwargs)
  def destroy(self, request, *args, **kwargs):
    print("CALL DESTROY(DELETE)")
    return super().destroy(request, *args, **kwargs)
# =========+=========+=========+=========+=========+

class TasksViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all() # FIX Model
  serializer_class  = TaskSerializer # FIX Serializer
  def retrieve(self, request, *args, **kwargs):
    print("CALL RETRIEVE(GET LIST)")
    return super().retrieve(request, *args, **kwargs)
# =========+=========+=========+=========+=========+

class PostsViewSet(viewsets.ModelViewSet):
  queryset = Posts.objects.all() # FIX Model
  serializer_class  = PostsSerializer # FIX Serializer
  def create(self, request, *args, **kwargs):
    print("CALL CREATE(POST)")
    return super().create(request, *args, **kwargs)
  def partial_update(self, request, *args, **kwargs):
    print("CALL PART UPD(PATCH)")
    return super().partial_update(request, *args, **kwargs)
# =========+=========+=========+=========+=========+

class PromptsViewSet(viewsets.ModelViewSet):
  queryset = Prompts.objects.all() # FIX Model
  serializer_class  = PromptsSerializer # FIX Serializer
  def create(self, request, *args, **kwargs):
    print("CALL CREATE(POST)")
    return super().create(request, *args, **kwargs)
  def partial_update(self, request, *args, **kwargs):
    print("CALL PART UPD(PATCH)")
    return super().partial_update(request, *args, **kwargs)
# =========+=========+=========+=========+=========+

class RequestsViewSet(viewsets.ModelViewSet):
  queryset = Requests.objects.all() # FIX Model
  serializer_class  = RequestsSerializer # FIX Serializer
  def create(self, request, *args, **kwargs):
    print("CALL CREATE(POST)")
    return super().create(request, *args, **kwargs)
  def partial_update(self, request, *args, **kwargs):
    print("CALL PART UPD(PATCH)")
    return super().partial_update(request, *args, **kwargs)
# =========+=========+=========+=========+=========+
