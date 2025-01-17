
from rest_framework import serializers
from .models import *

class BaseModelClassSerializer(serializers.ModelSerializer):
  class Meta:
    abstract = True
    model = BaseModelClass
    fields = ["id", "created_at", "updated_at", "deleted_at"]

# =========+=========+=========+=========+=========+
# Serializers
# =========+=========+=========+=========+=========+

class ConstantsSerializer(BaseModelClassSerializer):
  class Meta:
    model = Constants
    fields = ['Category', 'isLewd', 'Name', 'Value']
# =========+=========+=========+=========+=========+

class WeightsSerializer(BaseModelClassSerializer):
  class Meta:
    model = Weights
    fields = ['Model', 'Theme', 'Weathers', 'Periods', 'Angles', 'Directions', 'Focuses']
# =========+=========+=========+=========+=========+

class PhrasesSerializer(BaseModelClassSerializer):
  class Meta:
    model = Phrases
    fields = ['Header', 'Footer', 'Negative', 'RequestOrder', 'PlayingOrder', 'PostingDescription', 'ContentDescription']
# =========+=========+=========+=========+=========+

class GroupsSerializer(BaseModelClassSerializer):
  class Meta:
    model = Groups
    fields = ['name']
# =========+=========+=========+=========+=========+

class TaskSerializer(BaseModelClassSerializer):
  class Meta:
    model = Task
    fields = ['group_id', 'index', 'name']
# =========+=========+=========+=========+=========+

class PostsSerializer(BaseModelClassSerializer):
  class Meta:
    model = Posts
    fields = ['task_id', 'Story', 'TitleJP', 'TitleEN', 'TitleSymbol', 'PictureCount', 'WallpaperCount', 'PictureURL', 'WallpaperURL', 'Notes']
# =========+=========+=========+=========+=========+

class PromptsSerializer(BaseModelClassSerializer):
  class Meta:
    model = Prompts
    fields = ['task_id', 'HEADER', 'Basis', 'Faces', 'Hairs', 'Figures', 'Location', 'Outfits', 'Equips', 'Emotes', 'Fluids', 'Upper', 'Lower', 'Actions', 'Posing', 'Additional', 'FOOTER']
# =========+=========+=========+=========+=========+

class RequestsSerializer(BaseModelClassSerializer):
  class Meta:
    model = Requests
    fields = ['task_id']
# =========+=========+=========+=========+=========+

class BasisSerializer(BaseModelClassSerializer):
  class Meta:
    model = Basis
    fields = ['request_id', 'Model', 'Thickness', 'Theme', 'Species', 'SpeciesDetails', 'Traits', 'TraitsDetails']
# =========+=========+=========+=========+=========+

class LocationSerializer(BaseModelClassSerializer):
  class Meta:
    model = Location
    fields = ['request_id', 'Weathers', 'Periods', 'Times', 'LocationsDetails']
# =========+=========+=========+=========+=========+

class OutfitsSerializer(BaseModelClassSerializer):
  class Meta:
    model = Outfits
    fields = ['request_id', 'Jobs', 'JobsDetails', 'OutfitsDetails', 'EquipsDetails']
# =========+=========+=========+=========+=========+

class HairsSerializer(BaseModelClassSerializer):
  class Meta:
    model = Hairs
    fields = ['request_id', 'Size', 'HairStyle', 'BangsStyle']
# =========+=========+=========+=========+=========+

class FacesSerializer(BaseModelClassSerializer):
  class Meta:
    model = Faces
    fields = ['request_id', 'Looks', 'Eyes', 'Personality', 'Moods']
# =========+=========+=========+=========+=========+

class FiguresSerializer(BaseModelClassSerializer):
  class Meta:
    model = Figures
    fields = ['request_id', 'Thickness', 'Boobs', 'Bodies', 'Butts', 'SkinDetails']
# =========+=========+=========+=========+=========+

class UppersSerializer(BaseModelClassSerializer):
  class Meta:
    model = Uppers
    fields = ['request_id', 'Inverted', 'Puffy', 'Areola', 'Nipples']
# =========+=========+=========+=========+=========+

class LowersSerializer(BaseModelClassSerializer):
  class Meta:
    model = Lowers
    fields = ['request_id', 'Model', 'Public', 'Size', 'Sheath', 'Foreskin', 'GenitalDetails']
# =========+=========+=========+=========+=========+

class ColorsSerializer(BaseModelClassSerializer):
  class Meta:
    model = Colors
    fields = ['request_id', 'Theme', 'Hair', 'Eyes', 'OutfitsMain', 'OutfitsSub', 'EquipsMain', 'EquipsSub', 'SkinMain', 'SkinSub', 'Nipples', 'Genitals']
# =========+=========+=========+=========+=========+
