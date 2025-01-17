
from django.db import models
from django.core.exceptions import ValidationError

class BaseModelClass(models.Model):
  # === Base Properties ===
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  deleted_at = models.DateTimeField(null=True, blank=True)

  class Meta:
    abstract = True

  @classmethod
  def valid_list(target):
    if not isinstance(target, dict):
      raise ValidationError("This field must be a LIST...")
  @classmethod
  def valid_dict(target):
    if not isinstance(target, dict):
      raise ValidationError("This field must be a JSON...")

# =========+=========+=========+=========+=========+
# Models
# =========+=========+=========+=========+=========+

class Constants(BaseModelClass):
  # === Properties ===
  Category = models.TextField(default="", )
  isLewd = models.BooleanField(default=None, )
  Name = models.TextField(default="", )
  Value = models.TextField(default="", )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Weights(BaseModelClass):
  # === Properties ===
  Model = models.JSONField(validators=[BaseModelClass.valid_list], default=list, )
  Theme = models.JSONField(validators=[BaseModelClass.valid_list], default=list, )
  Weathers = models.JSONField(validators=[BaseModelClass.valid_list], default=list, )
  Periods = models.JSONField(validators=[BaseModelClass.valid_list], default=list, )
  Angles = models.JSONField(validators=[BaseModelClass.valid_list], default=list, )
  Directions = models.JSONField(validators=[BaseModelClass.valid_list], default=list, )
  Focuses = models.JSONField(validators=[BaseModelClass.valid_list], default=list, )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Phrases(BaseModelClass):
  # === Properties ===
  Header = models.TextField(default="", )
  Footer = models.TextField(default="", )
  Negative = models.TextField(default="", )
  RequestOrder = models.TextField(default="", )
  PlayingOrder = models.TextField(default="", )
  PostingDescription = models.TextField(default="", )
  ContentDescription = models.TextField(default="", )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Groups(BaseModelClass):
  # === Properties ===
  name = models.TextField(default="", )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Task(BaseModelClass):
  # === Properties ===
  group_id = models.FloatField(default=0, )
  index = models.FloatField(default=0, )
  name = models.TextField(default="", )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Posts(BaseModelClass):
  # === Properties ===
  task_id = models.FloatField(default=0, )
  Story = models.TextField(default="", )
  TitleJP = models.TextField(default="", )
  TitleEN = models.TextField(default="", )
  TitleSymbol = models.TextField(default="", )
  PictureCount = models.TextField(default="", )
  WallpaperCount = models.TextField(default="", )
  PictureURL = models.TextField(default="", )
  WallpaperURL = models.TextField(default="", )
  Notes = models.JSONField(validators=[BaseModelClass.valid_list], default=list, )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Prompts(BaseModelClass):
  # === Properties ===
  task_id = models.FloatField(default=0, )
  HEADER = models.TextField(default="", )
  Basis = models.TextField(default="", )
  Faces = models.TextField(default="", )
  Hairs = models.TextField(default="", )
  Figures = models.TextField(default="", )
  Location = models.TextField(default="", )
  Outfits = models.TextField(default="", )
  Equips = models.TextField(default="", )
  Emotes = models.TextField(default="", )
  Fluids = models.TextField(default="", )
  Upper = models.TextField(default="", )
  Lower = models.TextField(default="", )
  Actions = models.TextField(default="", )
  Posing = models.TextField(default="", )
  Additional = models.TextField(default="", )
  FOOTER = models.TextField(default="", )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Requests(BaseModelClass):
  # === Properties ===
  task_id = models.FloatField(default=0, )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Basis(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, )
  Model = models.FloatField(default=0, )
  Thickness = models.FloatField(default=0, )
  Theme = models.FloatField(default=0, )
  Species = models.TextField(default="", )
  SpeciesDetails = models.TextField(default="", )
  Traits = models.TextField(default="", )
  TraitsDetails = models.TextField(default="", )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Location(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, )
  Weathers = models.FloatField(default=0, )
  Periods = models.FloatField(default=0, )
  Times = models.FloatField(default=0, )
  LocationsDetails = models.TextField(default="", )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Outfits(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, )
  Jobs = models.TextField(default="", )
  JobsDetails = models.TextField(default="", )
  OutfitsDetails = models.TextField(default="", )
  EquipsDetails = models.TextField(default="", )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Hairs(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, )
  Size = models.FloatField(default=0, )
  HairStyle = models.TextField(default="", )
  BangsStyle = models.TextField(default="", )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Faces(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, )
  Looks = models.FloatField(default=0, )
  Eyes = models.FloatField(default=0, )
  Personality = models.FloatField(default=0, )
  Moods = models.FloatField(default=0, )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Figures(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, )
  Thickness = models.FloatField(default=0, )
  Boobs = models.FloatField(default=0, )
  Bodies = models.FloatField(default=0, )
  Butts = models.FloatField(default=0, )
  SkinDetails = models.TextField(default="", )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Uppers(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, )
  Inverted = models.FloatField(default=0, )
  Puffy = models.FloatField(default=0, )
  Areola = models.FloatField(default=0, )
  Nipples = models.FloatField(default=0, )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Lowers(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, )
  Model = models.FloatField(default=0, )
  Public = models.FloatField(default=0, )
  Size = models.FloatField(default=0, )
  Sheath = models.FloatField(default=0, )
  Foreskin = models.FloatField(default=0, )
  GenitalDetails = models.TextField(default="", )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Colors(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, )
  Theme = models.FloatField(default=0, )
  Hair = models.TextField(default="", )
  Eyes = models.TextField(default="", )
  OutfitsMain = models.TextField(default="", )
  OutfitsSub = models.TextField(default="", )
  EquipsMain = models.TextField(default="", )
  EquipsSub = models.TextField(default="", )
  SkinMain = models.TextField(default="", )
  SkinSub = models.TextField(default="", )
  Nipples = models.TextField(default="", )
  Genitals = models.TextField(default="", )

  # === Meta ===
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+
