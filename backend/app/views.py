
from rest_framework import viewsets
from .models import *
from .serializers import *

# =========+=========+=========+=========+=========+
# ViewSets
# =========+=========+=========+=========+=========+

class ConfigsViewSet(viewsets.ModelViewSet):
  queryset = BaseModelClass.objects.all() # FIX Model
  serializer_class  = BaseModelClass.objects.all() # FIX Serializer
# =========+=========+=========+=========+=========+

class GroupsViewSet(viewsets.ModelViewSet):
  queryset = BaseModelClass.objects.all() # FIX Model
  serializer_class  = BaseModelClass.objects.all() # FIX Serializer
# =========+=========+=========+=========+=========+

class TasksViewSet(viewsets.ModelViewSet):
  queryset = BaseModelClass.objects.all() # FIX Model
  serializer_class  = BaseModelClass.objects.all() # FIX Serializer
# =========+=========+=========+=========+=========+

class PostsViewSet(viewsets.ModelViewSet):
  queryset = BaseModelClass.objects.all() # FIX Model
  serializer_class  = BaseModelClass.objects.all() # FIX Serializer
# =========+=========+=========+=========+=========+

class PromptsViewSet(viewsets.ModelViewSet):
  queryset = BaseModelClass.objects.all() # FIX Model
  serializer_class  = BaseModelClass.objects.all() # FIX Serializer
# =========+=========+=========+=========+=========+

class RequestsViewSet(viewsets.ModelViewSet):
  queryset = BaseModelClass.objects.all() # FIX Model
  serializer_class  = BaseModelClass.objects.all() # FIX Serializer
# =========+=========+=========+=========+=========+
