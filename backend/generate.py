import yaml

from g_utils.g_model import generateModel
from g_utils.g_serializer import generateSerializer
from g_utils.g_views import generateView

def getSwaggerData():
  with open("swagger.yaml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)
    return data['info'], data['paths'], data['components']

if __name__ == "__main__":
  info, paths, components = getSwaggerData()
  generateModel(components)
  generateSerializer(components)
  generateView(paths)