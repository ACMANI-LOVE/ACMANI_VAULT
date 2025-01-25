from django.db import models
from django.core.exceptions import ValidationError


class BaseModelClass(models.Model):
    # === Base Properties ===
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # === Meta ===
    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
        return f"ID:[{self.id}] Created:[{self.created_at}] Delete:[{self.deleted_at}]"

    @classmethod
    def valid_list(self, target):
        if not isinstance(target, list):
            raise ValidationError("This field must be a LIST...")

    @classmethod
    def valid_dict(self, target):
        if not isinstance(target, dict):
            raise ValidationError("This field must be a JSON...")


# =========+=========+=========+=========+=========+
# Models
# =========+=========+=========+=========+=========+


class Constants(BaseModelClass):
    # === Properties ===
    category = models.TextField(default="")
    is_lewd = models.BooleanField(default=None)
    name = models.TextField(default="")
    value = models.TextField(default="")


# =========+=========+=========+=========+=========+


class Weights(BaseModelClass):
    # === Properties ===
    model = models.JSONField(validators=[BaseModelClass.valid_list], default=list)
    theme = models.JSONField(validators=[BaseModelClass.valid_list], default=list)
    weathers = models.JSONField(validators=[BaseModelClass.valid_list], default=list)
    periods = models.JSONField(validators=[BaseModelClass.valid_list], default=list)
    angles = models.JSONField(validators=[BaseModelClass.valid_list], default=list)
    directions = models.JSONField(validators=[BaseModelClass.valid_list], default=list)
    focuses = models.JSONField(validators=[BaseModelClass.valid_list], default=list)


# =========+=========+=========+=========+=========+


class Phrases(BaseModelClass):
    # === Properties ===
    header = models.TextField(default="")
    footer = models.TextField(default="")
    negative = models.TextField(default="")
    request_order = models.TextField(default="")
    playing_order = models.TextField(default="")
    posting_desc = models.TextField(default="")
    content_desc = models.TextField(default="")


# =========+=========+=========+=========+=========+


class Groups(BaseModelClass):
    # === Properties ===
    name = models.TextField(default="")


# =========+=========+=========+=========+=========+


class Task(BaseModelClass):
    # === Properties ===
    group_id = models.IntegerField(default=0)
    index = models.IntegerField(default=0)
    name = models.TextField(default="")


# =========+=========+=========+=========+=========+


class Posts(BaseModelClass):
    # === Properties ===
    task_id = models.IntegerField(default=0, unique=True)
    story = models.TextField(default="")
    title_JP = models.TextField(default="")
    title_EN = models.TextField(default="")
    title_symbol = models.TextField(default="")
    picture_count = models.TextField(default="")
    wallpaper_count = models.TextField(default="")
    picture_URL = models.TextField(default="")
    wallpaper_URL = models.TextField(default="")
    notes = models.JSONField(validators=[BaseModelClass.valid_list], default=list)


# =========+=========+=========+=========+=========+


class Prompts(BaseModelClass):
    # === Properties ===
    task_id = models.IntegerField(default=0, unique=True)
    HEADER = models.TextField(default="")
    basis = models.TextField(default="")
    faces = models.TextField(default="")
    hairs = models.TextField(default="")
    figures = models.TextField(default="")
    location = models.TextField(default="")
    outfits = models.TextField(default="")
    equips = models.TextField(default="")
    emotes = models.TextField(default="")
    fluids = models.TextField(default="")
    upper = models.TextField(default="")
    lower = models.TextField(default="")
    actions = models.TextField(default="")
    posing = models.TextField(default="")
    additional = models.TextField(default="")
    FOOTER = models.TextField(default="")


# =========+=========+=========+=========+=========+


class Requests(BaseModelClass):
    # === Properties ===
    task_id = models.IntegerField(default=0, unique=True)


# =========+=========+=========+=========+=========+
class Basis(BaseModelClass):
    # === Properties ===
    task_id = models.IntegerField(default=0, unique=True)
    model = models.IntegerField(default=0)
    thickness = models.IntegerField(default=0)
    theme = models.IntegerField(default=0)
    species = models.TextField(default="")
    species_details = models.TextField(default="")
    traits = models.TextField(default="")
    traits_details = models.TextField(default="")


# =========+=========+=========+=========+=========+


class Location(BaseModelClass):
    # === Properties ===
    task_id = models.IntegerField(default=0, unique=True)
    weathers = models.IntegerField(default=0)
    periods = models.IntegerField(default=0)
    times = models.IntegerField(default=0)
    locations_details = models.TextField(default="")


# =========+=========+=========+=========+=========+


class Outfits(BaseModelClass):
    # === Properties ===
    task_id = models.IntegerField(default=0, unique=True)
    jobs = models.TextField(default="")
    jobs_details = models.TextField(default="")
    outfits_details = models.TextField(default="")
    equips_details = models.TextField(default="")


# =========+=========+=========+=========+=========+


class Hairs(BaseModelClass):
    # === Properties ===
    task_id = models.IntegerField(default=0, unique=True)
    size = models.IntegerField(default=0)
    hair_style = models.TextField(default="")
    bangs_style = models.TextField(default="")


# =========+=========+=========+=========+=========+


class Faces(BaseModelClass):
    # === Properties ===
    task_id = models.IntegerField(default=0, unique=True)
    looks = models.IntegerField(default=0)
    eyes = models.IntegerField(default=0)
    personality = models.IntegerField(default=0)
    moods = models.IntegerField(default=0)


# =========+=========+=========+=========+=========+


class Figures(BaseModelClass):
    # === Properties ===
    task_id = models.IntegerField(default=0, unique=True)
    thickness = models.IntegerField(default=0)
    boobs = models.IntegerField(default=0)
    bodies = models.IntegerField(default=0)
    butts = models.IntegerField(default=0)
    skin_details = models.TextField(default="")


# =========+=========+=========+=========+=========+


class Uppers(BaseModelClass):
    # === Properties ===
    task_id = models.IntegerField(default=0, unique=True)
    inverted = models.IntegerField(default=0)
    puffy = models.IntegerField(default=0)
    areola = models.IntegerField(default=0)
    nipples = models.IntegerField(default=0)


# =========+=========+=========+=========+=========+


class Lowers(BaseModelClass):
    # === Properties ===
    task_id = models.IntegerField(default=0, unique=True)
    model = models.IntegerField(default=0)
    public = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    sheath = models.IntegerField(default=0)
    foreskin = models.IntegerField(default=0)
    genital_details = models.TextField(default="")


# =========+=========+=========+=========+=========+


class Colors(BaseModelClass):
    # === Properties ===
    task_id = models.IntegerField(default=0, unique=True)
    theme = models.IntegerField(default=0)
    hair = models.TextField(default="")
    eyes = models.TextField(default="")
    outfits_main = models.TextField(default="")
    outfits_sub = models.TextField(default="")
    equips_main = models.TextField(default="")
    equips_sub = models.TextField(default="")
    skin_main = models.TextField(default="")
    skin_sub = models.TextField(default="")
    nipples = models.TextField(default="")
    genitals = models.TextField(default="")


# =========+=========+=========+=========+=========+
