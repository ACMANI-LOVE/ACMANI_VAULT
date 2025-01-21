from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from .models import *
from .serializers import *

# =========+=========+=========+=========+=========+
# ViewSets
# =========+=========+=========+=========+=========+


class ConfigsViewSet(viewsets.ModelViewSet):
    queryset = Constants.objects.all()
    serializer_class = ConstantsSerializer

    # +=========+=========+=========+=========+=========
    # GET(retrieve)
    # +=========+=========+=========+=========+=========
    def retrieve(self, request, pk=None):
        try:
            constants = Constants.objects.all()
            phrases = Phrases.objects.order_by("id").first()
            weights = Weights.objects.order_by("id").first()
        except Constants.DoesNotExist or Phrases.DoesNotExist or Weights.DoesNotExist:
            return Response(
                {"message": "Models Does not Found."}, status=status.HTTP_404_NOT_FOUND
            )
        data = {
            "Constants": ConstantsSerializer(constants, many=True).data,
            "Phrases": PhrasesSerializer(phrases).data,
            "Weights": WeightsSerializer(weights).data,
        }
        return Response({"data": data}, status=status.HTTP_200_OK)

    # +=========+=========+=========+=========+=========
    # PUT(update)
    # +=========+=========+=========+=========+=========
    def update(self, request, pk=None):
        req_data = request.data
        try:
            tgt_phrases = Phrases.objects.first()
            tgt_weights = Weights.objects.first()
        except Phrases.DoesNotExist or Weights.DoesNotExist:
            return Response(
                {"message": "Models Does not Found."}, status=status.HTTP_404_NOT_FOUND
            )

        phrases = req_data.get("Phrases", {})
        weights = req_data.get("Weights", {})

        phrases_serializer = PhrasesSerializer(tgt_phrases, data=phrases, partial=False)
        weights_serializer = WeightsSerializer(tgt_weights, data=weights, partial=False)
        if phrases_serializer.is_valid() and weights_serializer.is_valid():
            phrases_serializer.save()
            weights_serializer.save()
            return Response({"message": "Update Success."}, status=status.HTTP_200_OK)

        return Response(
            {"message": "Update Failed."}, status=status.HTTP_400_BAD_REQUEST
        )

    # +=========+=========+=========+=========+=========
    # POST(create)
    # +=========+=========+=========+=========+=========
    def create(self, request, pk=None):
        req_data = request.data
        # Transaction Start
        with transaction.atomic():
            if "create" in req_data:
                for item in req_data.get("create", []):
                    serializer = ConstantsSerializer(data=item)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(
                            {"message": "Add Failed."},
                            status=status.HTTP_400_BAD_REQUEST,
                        )

            if "update" in req_data:
                for item in req_data.get("update", []):
                    try:
                        tgt_id = item.get("id")
                        target = Constants.objects.get(pk=tgt_id)
                        serializer = ConstantsSerializer(
                            target, data=item, partial=True
                        )
                        if serializer.is_valid():
                            serializer.save()
                        else:
                            return Response(
                                {"message": "Update Failed."},
                                status=status.HTTP_400_BAD_REQUEST,
                            )
                    except Constants.DoesNotExist:
                        return Response(
                            {"message": "Models Does not Found."},
                            status=status.HTTP_404_NOT_FOUND,
                        )

            if "delete" in req_data:
                for item in req_data.get("delete", []):
                    try:
                        tgt_id = item.get("id")
                        target = Constants.objects.get(pk=tgt_id)
                        target.delete()

                    except Constants.DoesNotExist:
                        return Response(
                            {"message": "Models Does not Found."},
                            status=status.HTTP_404_NOT_FOUND,
                        )

            return Response({"message": "Update Success."}, status=status.HTTP_200_OK)


# =========+=========+=========+=========+=========+


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer

    # +=========+=========+=========+=========+=========
    # GET(list)
    # +=========+=========+=========+=========+=========
    def list(self, request, pk=None):
        try:
            groups = Groups.objects.all()
            serializer = GroupsSerializer(groups, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Groups.DoesNotExist:
            return Response(
                {"message": "Models Does not Found."}, status=status.HTTP_404_NOT_FOUND
            )

    # +=========+=========+=========+=========+=========
    # POST(create)
    # +=========+=========+=========+=========+=========
    def create(self, request, pk=None):
        req_data = request.data
        serializer = GroupsSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Update Success."}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "Add Failed."}, status=status.HTTP_400_BAD_REQUEST
            )

    # +=========+=========+=========+=========+=========
    # PATCH(partial_update)
    # +=========+=========+=========+=========+=========
    def partial_update(self, request, pk=None):
        req_data = request.data
        try:
            target = Groups.objects.get(id=pk)
            serializer = GroupsSerializer(target, data=req_data, partial=True)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(
                    {"message": "Update Failed."}, status=status.HTTP_400_BAD_REQUEST
                )
        except Groups.DoesNotExist:
            return Response(
                {"message": "Models Does not Found."}, status=status.HTTP_404_NOT_FOUND
            )

    # +=========+=========+=========+=========+=========
    # DELETE(destroy)
    # +=========+=========+=========+=========+=========
    def destroy(self, request, pk=None):
        try:
            target = Groups.objects.get(id=pk)
            target.delete()
            return Response({"message": "Update Success."}, status=status.HTTP_200_OK)
        except Groups.DoesNotExist:
            return Response(
                {"message": "Models Does not Found."}, status=status.HTTP_404_NOT_FOUND
            )


# =========+=========+=========+=========+=========+


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # +=========+=========+=========+=========+=========
    # GET(list)
    # +=========+=========+=========+=========+=========
    def retrieve(self, request, pk=None):
        try:
            # Get Task Data
            task_list = Task.objects.filter(group_id=pk)

            task_data = []
            for task in task_list:
                task_id = task.get("id")
                if task_id is not None:
                    # Get Posting Data
                    post_data = PostsSerializer(Posts.objects.get(task_id=task_id)).data

                    # Get Prompt Data
                    prompt_data = PromptsSerializer(
                        Prompts.objects.get(task_id=task_id)
                    ).data

                    # Get Request Data
                    request_data = {
                        "basis": BasisSerializer(
                            Basis.objects.get(task_id=task_id)
                        ).data,
                        "location": LocationSerializer(
                            Location.objects.get(task_id=task_id)
                        ).data,
                        "outfits": OutfitsSerializer(
                            Outfits.objects.get(task_id=task_id)
                        ).data,
                        "hairs": HairsSerializer(
                            Hairs.objects.get(task_id=task_id)
                        ).data,
                        "faces": FacesSerializer(
                            Faces.objects.get(task_id=task_id)
                        ).data,
                        "figures": FiguresSerializer(
                            Figures.objects.get(task_id=task_id)
                        ).data,
                        "uppers": UppersSerializer(
                            Uppers.objects.get(task_id=task_id)
                        ).data,
                        "lowers": LowersSerializer(
                            Lowers.objects.get(task_id=task_id)
                        ).data,
                        "colors": ColorsSerializer(
                            Colors.objects.get(task_id=task_id)
                        ).data,
                    }
                    data = {
                        "task": TaskSerializer(task),
                        "post": post_data,
                        "prompt": prompt_data,
                        "request": request_data,
                    }
                else:
                    data = {
                        "task": TaskSerializer(task),
                        "post": None,
                        "prompt": None,
                        "request": None,
                    }
                task_data.append(data)
            return Response({"data": task_data}, status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response(
                {"message": "Models Does not Found."}, status=status.HTTP_404_NOT_FOUND
            )


# =========+=========+=========+=========+=========+


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def create(self, request, pk=None):
        req_data = request.data
        serializer = PostsSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Update Success."}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "Add Failed."}, status=status.HTTP_400_BAD_REQUEST
            )

    def partial_update(self, request, pk=None):
        req_data = request.data
        try:
            target = Posts.objects.get(pk=pk)
            serializer = PostsSerializer(target, data=req_data, partial=True)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(
                    {"message": "Update Failed."}, status=status.HTTP_400_BAD_REQUEST
                )
        except Posts.DoesNotExist:
            return Response(
                {"message": "Models Does not Found."}, status=status.HTTP_404_NOT_FOUND
            )


# =========+=========+=========+=========+=========+


class PromptsViewSet(viewsets.ModelViewSet):
    queryset = Prompts.objects.all()
    serializer_class = PromptsSerializer

    def create(self, request, pk=None):
        req_data = request.data
        serializer = PromptsSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Update Success."}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "Add Failed."}, status=status.HTTP_400_BAD_REQUEST
            )

    def partial_update(self, request, pk=None):
        req_data = request.data
        try:
            target = Prompts.objects.get(pk=pk)
            serializer = PromptsSerializer(target, data=req_data, partial=True)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(
                    {"message": "Update Failed."}, status=status.HTTP_400_BAD_REQUEST
                )
        except Prompts.DoesNotExist:
            return Response(
                {"message": "Models Does not Found."}, status=status.HTTP_404_NOT_FOUND
            )


# =========+=========+=========+=========+=========+


class RequestsViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, pk=None):
        req_data = request.data
        for key, item in req_data:
            match key:
                case "basis":
                    serializer = BasisSerializer(data=item)
                    break
                case "location":
                    serializer = LocationSerializer(data=item)
                    break
                case "outfits":
                    serializer = OutfitsSerializer(data=item)
                    break
                case "hairs":
                    serializer = HairsSerializer(data=item)
                    break
                case "faces":
                    serializer = FacesSerializer(data=item)
                    break
                case "figures":
                    serializer = FiguresSerializer(data=item)
                    break
                case "uppers":
                    serializer = UppersSerializer(data=item)
                    break
                case "lowers":
                    serializer = LowersSerializer(data=item)
                    break
                case "colors":
                    serializer = ColorsSerializer(data=item)
                    break
                case _:
                    return Response(
                        {"message": "Add Failed."}, status=status.HTTP_400_BAD_REQUEST
                    )

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(
                    {"message": "Add Failed."}, status=status.HTTP_400_BAD_REQUEST
                )
        return Response({"message": "Update Success."}, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        req_data = request.data
        try:
            for key, item in req_data:
                match key:
                    case "basis":
                        target = Basis.objects.get(task_id=pk)
                        serializer = BasisSerializer(target, data=item, partial=True)
                        break
                    case "location":
                        target = Location.objects.get(task_id=pk)
                        serializer = LocationSerializer(target, data=item, partial=True)
                        break
                    case "outfits":
                        target = Outfits.objects.get(task_id=pk)
                        serializer = OutfitsSerializer(target, data=item, partial=True)
                        break
                    case "hairs":
                        target = Hairs.objects.get(task_id=pk)
                        serializer = HairsSerializer(target, data=item, partial=True)
                        break
                    case "faces":
                        target = Faces.objects.get(task_id=pk)
                        serializer = FacesSerializer(target, data=item, partial=True)
                        break
                    case "figures":
                        target = Figures.objects.get(task_id=pk)
                        serializer = FiguresSerializer(target, data=item, partial=True)
                        break
                    case "uppers":
                        target = Uppers.objects.get(task_id=pk)
                        serializer = UppersSerializer(target, data=item, partial=True)
                        break
                    case "lowers":
                        target = Lowers.objects.get(task_id=pk)
                        serializer = LowersSerializer(target, data=item, partial=True)
                        break
                    case "colors":
                        target = Colors.objects.get(task_id=pk)
                        serializer = ColorsSerializer(target, data=item, partial=True)
                        break
                    case _:
                        return Response(
                            {"message": "Add Failed."},
                            status=status.HTTP_400_BAD_REQUEST,
                        )

                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(
                        {"message": "Update Failed."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
        except:
            return Response(
                {"message": "Update Failed."}, status=status.HTTP_400_BAD_REQUEST
            )


# =========+=========+=========+=========+=========+
