
from rest_framework import viewsets
from .models import *
from .serializers import *

# =========+=========+=========+=========+=========+
# ViewSets
# =========+=========+=========+=========+=========+

class ConfigsViewSet(viewsets.ModelViewSet):
  queryset = Constants.objects.all() # FIX Model
  serializer_class  = ConstantsSerializer # FIX Serializer
# =========+=========+=========+=========+=========+

class GroupsViewSet(viewsets.ModelViewSet):
  queryset = Groups.objects.all() # FIX Model
  serializer_class  = GroupsSerializer # FIX Serializer
# =========+=========+=========+=========+=========+

class TasksViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all() # FIX Model
  serializer_class  = TaskSerializer # FIX Serializer
# =========+=========+=========+=========+=========+

class PostsViewSet(viewsets.ModelViewSet):
  queryset = Posts.objects.all() # FIX Model
  serializer_class  = PostsSerializer # FIX Serializer
# =========+=========+=========+=========+=========+

class PromptsViewSet(viewsets.ModelViewSet):
  queryset = Prompts.objects.all() # FIX Model
  serializer_class  = PromptsSerializer # FIX Serializer
# =========+=========+=========+=========+=========+

class RequestsViewSet(viewsets.ModelViewSet):
  queryset = Requests.objects.all() # FIX Model
  serializer_class  = RequestsSerializer # FIX Serializer
# =========+=========+=========+=========+=========+
