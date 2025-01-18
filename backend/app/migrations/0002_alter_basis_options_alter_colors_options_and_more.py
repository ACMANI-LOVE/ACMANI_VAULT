# Generated by Django 5.1.5 on 2025-01-18 06:31

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="basis", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="colors", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="constants", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="faces", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="figures", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="groups", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="hairs", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="location", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="lowers", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="outfits", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="phrases", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="posts", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="prompts", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="requests", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="task", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="uppers", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="weights", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterField(
            model_name="basis", name="Model", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="basis", name="Species", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="basis",
            name="SpeciesDetails",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="basis", name="Theme", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="basis", name="Thickness", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="basis", name="Traits", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="basis",
            name="TraitsDetails",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="basis", name="request_id", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="colors", name="EquipsMain", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="colors", name="EquipsSub", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="colors", name="Eyes", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="colors", name="Genitals", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="colors", name="Hair", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="colors", name="Nipples", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="colors", name="OutfitsMain", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="colors", name="OutfitsSub", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="colors", name="SkinMain", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="colors", name="SkinSub", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="colors", name="Theme", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="colors", name="request_id", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="constants", name="Category", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="constants", name="Name", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="constants", name="Value", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="constants",
            name="isLewd",
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name="faces", name="Eyes", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="faces", name="Looks", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="faces", name="Moods", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="faces", name="Personality", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="faces", name="request_id", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="figures", name="Bodies", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="figures", name="Boobs", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="figures", name="Butts", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="figures",
            name="SkinDetails",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="figures", name="Thickness", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="figures", name="request_id", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="groups", name="name", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="hairs", name="BangsStyle", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="hairs", name="HairStyle", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="hairs", name="Size", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="hairs", name="request_id", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="location",
            name="LocationsDetails",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="location", name="Periods", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="location", name="Times", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="location", name="Weathers", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="location",
            name="request_id",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="lowers", name="Foreskin", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="lowers",
            name="GenitalDetails",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="lowers", name="Model", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="lowers", name="Public", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="lowers", name="Sheath", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="lowers", name="Size", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="lowers", name="request_id", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="outfits",
            name="EquipsDetails",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="outfits", name="Jobs", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="outfits",
            name="JobsDetails",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="outfits",
            name="OutfitsDetails",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="outfits", name="request_id", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="phrases",
            name="ContentDescription",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="phrases", name="Footer", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="phrases", name="Header", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="phrases", name="Negative", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="phrases",
            name="PlayingOrder",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="phrases",
            name="PostingDescription",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="phrases",
            name="RequestOrder",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="posts",
            name="Notes",
            field=models.JSONField(
                default=list, validators=[app.models.BaseModelClass.valid_list]
            ),
        ),
        migrations.AlterField(
            model_name="posts", name="PictureCount", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="posts", name="PictureURL", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="posts", name="Story", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="posts", name="TitleEN", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="posts", name="TitleJP", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="posts", name="TitleSymbol", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="posts",
            name="WallpaperCount",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="posts", name="WallpaperURL", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="posts", name="task_id", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="prompts", name="Actions", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Additional", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Basis", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Emotes", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Equips", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="FOOTER", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Faces", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Figures", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Fluids", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="HEADER", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Hairs", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Location", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Lower", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Outfits", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Posing", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="Upper", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="prompts", name="task_id", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="requests", name="task_id", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="task", name="group_id", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="task", name="index", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="task", name="name", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="uppers", name="Areola", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="uppers", name="Inverted", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="uppers", name="Nipples", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="uppers", name="Puffy", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="uppers", name="request_id", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="weights",
            name="Angles",
            field=models.JSONField(
                default=list, validators=[app.models.BaseModelClass.valid_list]
            ),
        ),
        migrations.AlterField(
            model_name="weights",
            name="Directions",
            field=models.JSONField(
                default=list, validators=[app.models.BaseModelClass.valid_list]
            ),
        ),
        migrations.AlterField(
            model_name="weights",
            name="Focuses",
            field=models.JSONField(
                default=list, validators=[app.models.BaseModelClass.valid_list]
            ),
        ),
        migrations.AlterField(
            model_name="weights",
            name="Model",
            field=models.JSONField(
                default=list, validators=[app.models.BaseModelClass.valid_list]
            ),
        ),
        migrations.AlterField(
            model_name="weights",
            name="Periods",
            field=models.JSONField(
                default=list, validators=[app.models.BaseModelClass.valid_list]
            ),
        ),
        migrations.AlterField(
            model_name="weights",
            name="Theme",
            field=models.JSONField(
                default=list, validators=[app.models.BaseModelClass.valid_list]
            ),
        ),
        migrations.AlterField(
            model_name="weights",
            name="Weathers",
            field=models.JSONField(
                default=list, validators=[app.models.BaseModelClass.valid_list]
            ),
        ),
    ]
