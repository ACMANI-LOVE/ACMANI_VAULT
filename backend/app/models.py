
from django.db import models
from django.core.exceptions import ValidationError

class BaseModelClass(models.Model):
  # === Base Properties ===
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  deleted_at = models.DateTimeField(null=True, blank=True)

  class Meta:
    abstract = True

  def valid_list(target):
    if not isinstance(target, dict):
      raise ValidationError("This field must be a LIST...")
  def valid_dict(target):
    if not isinstance(target, dict):
      raise ValidationError("This field must be a JSON...")

# =========+=========+=========+=========+=========+
# Models
# =========+=========+=========+=========+=========+

class Constants(BaseModelClass):
  # === Properties ===
  id = models.FloatField(default=0, verbose_name="None")
  Category = models.TextField(default="", verbose_name="None")
  isLewd = models.BooleanField(default=None, verbose_name="None")
  Name = models.TextField(default="", verbose_name="None")
  Value = models.TextField(default="", verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Weights(BaseModelClass):
  # === Properties ===
  Model = models.JSONField(validators=[BaseModelClass().valid_list], default=list, verbose_name="None")
  Theme = models.JSONField(validators=[BaseModelClass().valid_list], default=list, verbose_name="None")
  Weathers = models.JSONField(validators=[BaseModelClass().valid_list], default=list, verbose_name="None")
  Periods = models.JSONField(validators=[BaseModelClass().valid_list], default=list, verbose_name="None")
  Angles = models.JSONField(validators=[BaseModelClass().valid_list], default=list, verbose_name="None")
  Directions = models.JSONField(validators=[BaseModelClass().valid_list], default=list, verbose_name="None")
  Focuses = models.JSONField(validators=[BaseModelClass().valid_list], default=list, verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Phrases(BaseModelClass):
  # === Properties ===
  Header = models.TextField(default="", verbose_name="None")
  Footer = models.TextField(default="", verbose_name="None")
  Negative = models.TextField(default="", verbose_name="None")
  RequestOrder = models.TextField(default="", verbose_name="None")
  PlayingOrder = models.TextField(default="", verbose_name="None")
  PostingDescription = models.TextField(default="", verbose_name="None")
  ContentDescription = models.TextField(default="", verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Groups(BaseModelClass):
  # === Properties ===
  id = models.FloatField(default=0, verbose_name="None")
  name = models.TextField(default="", verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Task(BaseModelClass):
  # === Properties ===
  id = models.FloatField(default=0, verbose_name="None")
  group_id = models.FloatField(default=0, verbose_name="None")
  index = models.FloatField(default=0, verbose_name="None")
  name = models.TextField(default="", verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Posts(BaseModelClass):
  # === Properties ===
  id = models.FloatField(default=0, verbose_name="None")
  task_id = models.FloatField(default=0, verbose_name="None")
  Story = models.TextField(default="", verbose_name="None")
  TitleJP = models.TextField(default="", verbose_name="None")
  TitleEN = models.TextField(default="", verbose_name="None")
  TitleSymbol = models.TextField(default="", verbose_name="None")
  PictureCount = models.TextField(default="", verbose_name="None")
  WallpaperCount = models.TextField(default="", verbose_name="None")
  PictureURL = models.TextField(default="", verbose_name="None")
  WallpaperURL = models.TextField(default="", verbose_name="None")
  Notes = models.JSONField(validators=[BaseModelClass().valid_list], default=list, verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Prompts(BaseModelClass):
  # === Properties ===
  id = models.FloatField(default=0, verbose_name="None")
  task_id = models.FloatField(default=0, verbose_name="None")
  HEADER = models.TextField(default="", verbose_name="None")
  Basis = models.TextField(default="", verbose_name="None")
  Faces = models.TextField(default="", verbose_name="None")
  Hairs = models.TextField(default="", verbose_name="None")
  Figures = models.TextField(default="", verbose_name="None")
  Location = models.TextField(default="", verbose_name="None")
  Outfits = models.TextField(default="", verbose_name="None")
  Equips = models.TextField(default="", verbose_name="None")
  Emotes = models.TextField(default="", verbose_name="None")
  Fluids = models.TextField(default="", verbose_name="None")
  Upper = models.TextField(default="", verbose_name="None")
  Lower = models.TextField(default="", verbose_name="None")
  Actions = models.TextField(default="", verbose_name="None")
  Posing = models.TextField(default="", verbose_name="None")
  Additional = models.TextField(default="", verbose_name="None")
  FOOTER = models.TextField(default="", verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Requests(BaseModelClass):
  # === Properties ===
  id = models.FloatField(default=0, verbose_name="None")
  task_id = models.FloatField(default=0, verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Basis(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, verbose_name="None")
  Model = models.FloatField(default=0, verbose_name="None")
  Thickness = models.FloatField(default=0, verbose_name="None")
  Theme = models.FloatField(default=0, verbose_name="None")
  Species = models.TextField(default="", verbose_name="None")
  SpeciesDetails = models.TextField(default="", verbose_name="None")
  Traits = models.TextField(default="", verbose_name="None")
  TraitsDetails = models.TextField(default="", verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Location(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, verbose_name="None")
  Weathers = models.FloatField(default=0, verbose_name="None")
  Periods = models.FloatField(default=0, verbose_name="None")
  Times = models.FloatField(default=0, verbose_name="None")
  LocationsDetails = models.TextField(default="", verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Outfits(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, verbose_name="None")
  Jobs = models.TextField(default="", verbose_name="None")
  JobsDetails = models.TextField(default="", verbose_name="None")
  OutfitsDetails = models.TextField(default="", verbose_name="None")
  EquipsDetails = models.TextField(default="", verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Hairs(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, verbose_name="None")
  Size = models.FloatField(default=0, verbose_name="None")
  HairStyle = models.TextField(default="", verbose_name="None")
  BangsStyle = models.TextField(default="", verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Faces(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, verbose_name="None")
  Looks = models.FloatField(default=0, verbose_name="None")
  Eyes = models.FloatField(default=0, verbose_name="None")
  Personality = models.FloatField(default=0, verbose_name="None")
  Moods = models.FloatField(default=0, verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Figures(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, verbose_name="None")
  Thickness = models.FloatField(default=0, verbose_name="None")
  Boobs = models.FloatField(default=0, verbose_name="None")
  Bodies = models.FloatField(default=0, verbose_name="None")
  Butts = models.FloatField(default=0, verbose_name="None")
  SkinDetails = models.TextField(default="", verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Uppers(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, verbose_name="None")
  Inverted = models.FloatField(default=0, verbose_name="None")
  Puffy = models.FloatField(default=0, verbose_name="None")
  Areola = models.FloatField(default=0, verbose_name="None")
  Nipples = models.FloatField(default=0, verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Lowers(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, verbose_name="None")
  Model = models.FloatField(default=0, verbose_name="None")
  Public = models.FloatField(default=0, verbose_name="None")
  Size = models.FloatField(default=0, verbose_name="None")
  Sheath = models.FloatField(default=0, verbose_name="None")
  Foreskin = models.FloatField(default=0, verbose_name="None")
  GenitalDetails = models.TextField(default="", verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+

class Colors(BaseModelClass):
  # === Properties ===
  request_id = models.FloatField(default=0, verbose_name="None")
  Theme = models.FloatField(default=0, verbose_name="None")
  Hair = models.TextField(default="", verbose_name="None")
  Eyes = models.TextField(default="", verbose_name="None")
  OutfitsMain = models.TextField(default="", verbose_name="None")
  OutfitsSub = models.TextField(default="", verbose_name="None")
  EquipsMain = models.TextField(default="", verbose_name="None")
  EquipsSub = models.TextField(default="", verbose_name="None")
  SkinMain = models.TextField(default="", verbose_name="None")
  SkinSub = models.TextField(default="", verbose_name="None")
  Nipples = models.TextField(default="", verbose_name="None")
  Genitals = models.TextField(default="", verbose_name="None")

  # === Meta ===
  class Meta:
    verbose_name = "None"
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.name}"
# =========+=========+=========+=========+=========+
