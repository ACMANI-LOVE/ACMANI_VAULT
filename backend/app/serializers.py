from rest_framework import serializers
from .models import *


class BaseModelClassSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        model = BaseModelClass
        fields = [
            "id",
            "created_at",
            "updated_at",
            "deleted_at",
        ]


# =========+=========+=========+=========+=========+
# Serializers
# =========+=========+=========+=========+=========+


class ConstantsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Constants
        fields = "__all__"


# =========+=========+=========+=========+=========+


class WeightsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Weights
        fields = "__all__"


# =========+=========+=========+=========+=========+


class PhrasesSerializer(BaseModelClassSerializer):
    class Meta:
        model = Phrases
        fields = "__all__"


# =========+=========+=========+=========+=========+


class GroupsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Groups
        fields = "__all__"


# =========+=========+=========+=========+=========+


class TaskSerializer(BaseModelClassSerializer):
    class Meta:
        model = Task
        fields = "__all__"


# =========+=========+=========+=========+=========+


class PostsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Posts
        fields = "__all__"


# =========+=========+=========+=========+=========+


class PromptsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Prompts
        fields = "__all__"


# =========+=========+=========+=========+=========+


class RequestsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Requests
        fields = "__all__"


# =========+=========+=========+=========+=========+
class BasisSerializer(BaseModelClassSerializer):
    class Meta:
        model = Basis
        fields = "__all__"


# =========+=========+=========+=========+=========+


class LocationSerializer(BaseModelClassSerializer):
    class Meta:
        model = Location
        fields = "__all__"


# =========+=========+=========+=========+=========+


class OutfitsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Outfits
        fields = "__all__"


# =========+=========+=========+=========+=========+


class HairsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Hairs
        fields = "__all__"


# =========+=========+=========+=========+=========+


class FacesSerializer(BaseModelClassSerializer):
    class Meta:
        model = Faces
        fields = "__all__"


# =========+=========+=========+=========+=========+


class FiguresSerializer(BaseModelClassSerializer):
    class Meta:
        model = Figures
        fields = "__all__"


# =========+=========+=========+=========+=========+


class UppersSerializer(BaseModelClassSerializer):
    class Meta:
        model = Uppers
        fields = "__all__"


# =========+=========+=========+=========+=========+


class LowersSerializer(BaseModelClassSerializer):
    class Meta:
        model = Lowers
        fields = "__all__"


# =========+=========+=========+=========+=========+


class ColorsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Colors
        fields = "__all__"


# =========+=========+=========+=========+=========+
