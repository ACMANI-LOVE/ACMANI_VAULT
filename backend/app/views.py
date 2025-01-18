
from rest_framework import viewsets
from .models import *
from .serializers import *

# =========+=========+=========+=========+=========+
# ViewSets
# =========+=========+=========+=========+=========+

class ConfigsViewSet(viewsets.ModelViewSet):
  queryset = Constants.objects.all() # FIX Model
  serializer_class  = ConstantsSerializer # FIX Serializer
  def list(self, request, *args, **kwargs):
    print("CALL LIST(GET)")
    return super().list(request, *args, **kwargs)
  def update(self, request, *args, **kwargs):
    print("CALL UPDATE(PUT)")
    return super().update(request, *args, **kwargs)
  def create(self, request, *args, **kwargs):
    print("CALL CREATE(POST)")
    return super().create(request, *args, **kwargs)
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
