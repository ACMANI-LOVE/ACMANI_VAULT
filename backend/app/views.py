
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from .models import *
from .serializers import *

# =========+=========+=========+=========+=========+
# ViewSets
# =========+=========+=========+=========+=========+

class ConfigsViewSet(viewsets.ModelViewSet):
  queryset = Constants.objects.all()
  serializer_class  = ConstantsSerializer

  def list(self, _):
    try:
      constants = Constants.objects.all()
      phrases   = Phrases.objects.order_by("id").first()
      weights   = Weights.objects.order_by("id").first()
    except Constants.DoesNotExist | Phrases.DoesNotExist | Weights.DoesNotExist:
      return Response({"message":"Models Does not Found."}, status=status.HTTP_404_NOT_FOUND)
    constants_data = ConstantsSerializer(constants, many=True)
    phrases_data   = PhrasesSerializer(phrases)
    weights_data   = WeightsSerializer(weights)
    data = {
      "Constants":constants_data.data,
      "Phrases":  phrases_data.data,
      "Weights":  weights_data.data
    }
    return Response([data], status=status.HTTP_200_OK)

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

  def create(self, request):
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
  queryset = Groups.objects.all()
  serializer_class  = GroupsSerializer

  def list(self, _):
    try:
      groups = Groups.objects.all()
      serializer = GroupsSerializer(groups, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Groups.DoesNotExist:
        return Response({"message":"Models Does not Found."}, status=status.HTTP_404_NOT_FOUND)

  def create(self, request):
    req_data = request.data
    serializer = GroupsSerializer(data=req_data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message":"Update Success."}, status=status.HTTP_200_OK)
    else:
      return Response({"message":"Add Failed."}, status=status.HTTP_400_BAD_REQUEST)

  def partial_update(self, request, pk=None):
    req_data = request.data
    try:
      target = Groups.objects.get(pk=pk)
      serializer = GroupsSerializer(target, data=req_data, partial=True)
      if serializer.is_valid():
        serializer.save()
      else:
        return Response({"message":"Update Failed."}, status=status.HTTP_400_BAD_REQUEST)
    except Groups.DoesNotExist:
        return Response({"message":"Models Does not Found."}, status=status.HTTP_404_NOT_FOUND)

  def destroy(self, _, pk=None):
    try:
      target = Groups.objects.get(pk=pk)
      target.delete()
      return Response({"message":"Update Success."}, status=status.HTTP_200_OK)
    except Groups.DoesNotExist:
        return Response({"message":"Models Does not Found."}, status=status.HTTP_404_NOT_FOUND)
# =========+=========+=========+=========+=========+

class TasksViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class  = TaskSerializer

  def retrieve(self, _, pk=None):
    try:
      task_list = Task.objects.filter(group_id=pk)
      serializer = TaskSerializer(task_list, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({"message":"Models Does not Found."}, status=status.HTTP_404_NOT_FOUND)
# =========+=========+=========+=========+=========+

class PostsViewSet(viewsets.ModelViewSet):
  queryset = Posts.objects.all()
  serializer_class  = PostsSerializer

  def create(self, request):
    req_data = request.data
    serializer = PostsSerializer(data=req_data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message":"Update Success."}, status=status.HTTP_200_OK)
    else:
      return Response({"message":"Add Failed."}, status=status.HTTP_400_BAD_REQUEST)
  def partial_update(self, request, pk=None):
    req_data = request.data
    try:
      target = Posts.objects.get(pk=pk)
      serializer = PostsSerializer(target, data=req_data, partial=True)
      if serializer.is_valid():
        serializer.save()
      else:
        return Response({"message":"Update Failed."}, status=status.HTTP_400_BAD_REQUEST)
    except Posts.DoesNotExist:
        return Response({"message":"Models Does not Found."}, status=status.HTTP_404_NOT_FOUND)
# =========+=========+=========+=========+=========+

class PromptsViewSet(viewsets.ModelViewSet):
  queryset = Prompts.objects.all()
  serializer_class  = PromptsSerializer

  def create(self, request):
    req_data = request.data
    serializer = PromptsSerializer(data=req_data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message":"Update Success."}, status=status.HTTP_200_OK)
    else:
      return Response({"message":"Add Failed."}, status=status.HTTP_400_BAD_REQUEST)
  def partial_update(self, request, pk=None):
    req_data = request.data
    try:
      target = Prompts.objects.get(pk=pk)
      serializer = PromptsSerializer(target, data=req_data, partial=True)
      if serializer.is_valid():
        serializer.save()
      else:
        return Response({"message":"Update Failed."}, status=status.HTTP_400_BAD_REQUEST)
    except Prompts.DoesNotExist:
        return Response({"message":"Models Does not Found."}, status=status.HTTP_404_NOT_FOUND)
# =========+=========+=========+=========+=========+

class RequestsViewSet(viewsets.ModelViewSet):
  queryset = Requests.objects.all()
  serializer_class  = RequestsSerializer

  def create(self, request):
    req_data = request.data
    serializer = RequestsSerializer(data=req_data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message":"Update Success."}, status=status.HTTP_200_OK)
    else:
      return Response({"message":"Add Failed."}, status=status.HTTP_400_BAD_REQUEST)
  def partial_update(self, request, pk=None):
    req_data = request.data
    try:
      target = Requests.objects.get(pk=pk)
      serializer = RequestsSerializer(target, data=req_data, partial=True)
      if serializer.is_valid():
        serializer.save()
      else:
        return Response({"message":"Update Failed."}, status=status.HTTP_400_BAD_REQUEST)
    except Requests.DoesNotExist:
        return Response({"message":"Models Does not Found."}, status=status.HTTP_404_NOT_FOUND)
# =========+=========+=========+=========+=========+
