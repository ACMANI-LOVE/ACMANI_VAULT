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
        fields = [
            "category",
            "is_lewd",
            "name",
            "value",
        ]


# =========+=========+=========+=========+=========+


class WeightsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Weights
        fields = [
            "model",
            "theme",
            "weathers",
            "periods",
            "angles",
            "directions",
            "focuses",
        ]


# =========+=========+=========+=========+=========+


class PhrasesSerializer(BaseModelClassSerializer):
    class Meta:
        model = Phrases
        fields = [
            "header",
            "footer",
            "negative",
            "request_order",
            "playing_order",
            "posting_desc",
            "content_desc",
        ]


# =========+=========+=========+=========+=========+


class GroupsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Groups
        fields = ["name"]


# =========+=========+=========+=========+=========+


class TaskSerializer(BaseModelClassSerializer):
    class Meta:
        model = Task
        fields = ["group_id", "index", "name"]


# =========+=========+=========+=========+=========+


class PostsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Posts
        fields = [
            "task_id",
            "story",
            "title_JP",
            "title_EN",
            "title_symbol",
            "picture_count",
            "wallpaper_count",
            "picture_URL",
            "wallpaper_URL",
            "notes",
        ]


# =========+=========+=========+=========+=========+


class PromptsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Prompts
        fields = [
            "task_id",
            "HEADER",
            "basis",
            "faces",
            "hairs",
            "figures",
            "location",
            "outfits",
            "equips",
            "emotes",
            "fluids",
            "upper",
            "lower",
            "actions",
            "posing",
            "additional",
            "FOOTER",
        ]


# =========+=========+=========+=========+=========+


class BasisSerializer(BaseModelClassSerializer):
    class Meta:
        model = Basis
        fields = [
            "task_id",
            "model",
            "thickness",
            "theme",
            "species",
            "species_details",
            "traits",
            "traits_details",
        ]


# =========+=========+=========+=========+=========+


class LocationSerializer(BaseModelClassSerializer):
    class Meta:
        model = Location
        fields = [
            "task_id",
            "weathers",
            "periods",
            "times",
            "locations_details",
        ]


# =========+=========+=========+=========+=========+


class OutfitsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Outfits
        fields = [
            "task_id",
            "jobs",
            "jobs_details",
            "outfits_details",
            "equips_details",
        ]


# =========+=========+=========+=========+=========+


class HairsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Hairs
        fields = [
            "task_id",
            "size",
            "hair_style",
            "bangs_style",
        ]


# =========+=========+=========+=========+=========+


class FacesSerializer(BaseModelClassSerializer):
    class Meta:
        model = Faces
        fields = [
            "task_id",
            "looks",
            "eyes",
            "personality",
            "moods",
        ]


# =========+=========+=========+=========+=========+


class FiguresSerializer(BaseModelClassSerializer):
    class Meta:
        model = Figures
        fields = [
            "task_id",
            "thickness",
            "boobs",
            "bodies",
            "butts",
            "skin_details",
        ]


# =========+=========+=========+=========+=========+


class UppersSerializer(BaseModelClassSerializer):
    class Meta:
        model = Uppers
        fields = [
            "task_id",
            "inverted",
            "puffy",
            "areola",
            "nipples",
        ]


# =========+=========+=========+=========+=========+


class LowersSerializer(BaseModelClassSerializer):
    class Meta:
        model = Lowers
        fields = [
            "task_id",
            "model",
            "public",
            "size",
            "sheath",
            "foreskin",
            "genital_details",
        ]


# =========+=========+=========+=========+=========+


class ColorsSerializer(BaseModelClassSerializer):
    class Meta:
        model = Colors
        fields = [
            "task_id",
            "theme",
            "hair",
            "eyes",
            "outfits_main",
            "outfits_sub",
            "equips_main",
            "equips_sub",
            "skin_main",
            "skin_sub",
            "nipples",
            "genitals",
        ]


# =========+=========+=========+=========+=========+
