from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from .models import *
from .serializers import *

# =========+=========+=========+=========+=========+
# ViewSets
# =========+=========+=========+=========+=========+


class ConfigsViewSet(viewsets.ModelViewSet):
    queryset = Constants.objects.none()
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
                {
                    "message": "Models Does not Found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        data = {
            "Constants": ConstantsSerializer(constants, many=True).data,
            "Phrases": PhrasesSerializer(phrases).data,
            "Weights": WeightsSerializer(weights).data,
        }
        return Response(
            {
                "data": data,
            },
            status=status.HTTP_200_OK,
        )

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
                {
                    "message": "Models Does not Found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        phrases = req_data.get("phrases", {})
        weights = req_data.get("weights", {})

        phrases_serializer = PhrasesSerializer(tgt_phrases, data=phrases, partial=False)
        weights_serializer = WeightsSerializer(tgt_weights, data=weights, partial=False)
        if phrases_serializer.is_valid() and weights_serializer.is_valid():
            phrases_serializer.save()
            weights_serializer.save()
            return Response(
                {
                    "message": "Update Success.",
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                "message": "Update Failed.",
            },
            status=status.HTTP_400_BAD_REQUEST,
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
                                {
                                    "message": "Update Failed.",
                                },
                                status=status.HTTP_400_BAD_REQUEST,
                            )
                    except Constants.DoesNotExist:
                        return Response(
                            {
                                "message": "Models Does not Found.",
                            },
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
                            {
                                "message": "Models Does not Found.",
                            },
                            status=status.HTTP_404_NOT_FOUND,
                        )

            return Response(
                {
                    "message": "Update Success.",
                },
                status=status.HTTP_200_OK,
            )


# =========+=========+=========+=========+=========+


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.none()
    serializer_class = GroupsSerializer

    # +=========+=========+=========+=========+=========
    # GET(list)
    # +=========+=========+=========+=========+=========
    def list(self, request, pk=None):
        try:
            groups = Groups.objects.all()
            serializer = GroupsSerializer(groups, many=True)
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Groups.DoesNotExist:
            return Response(
                {
                    "message": "Models Does not Found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    # +=========+=========+=========+=========+=========
    # POST(create)
    # +=========+=========+=========+=========+=========
    def create(self, request, pk=None):
        req_data = request.data
        try:
            with transaction.atomic():
                serializer = GroupsSerializer(data=req_data)
                if serializer.is_valid():
                    created_group = serializer.save()
                    task_name = created_group.name  # YYYY:MMM_DDth - MMM_DDth
                    task_list = []
                    for index in range(8):
                        task_list.append(
                            {
                                "group_id": created_group.id,
                                "index": index,
                                "name": f"Task_{str(index+1).zfill(2)}",
                            }
                        )

                    taskSerializer = TaskSerializer(data=task_list, many=True)
                    if taskSerializer.is_valid():
                        created_task = taskSerializer.save()
                        return Response(
                            {
                                "message": "Add Success.",
                            },
                            status=status.HTTP_200_OK,
                        )
                    else:
                        print(taskSerializer.errors)
                        return Response(
                            {
                                "message": "Add Failed.",
                            },
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                else:
                    return Response(
                        {
                            "message": "Add Failed.",
                            "error": serializer.errors,
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
        except Exception as Err:
            return Response(
                {
                    "message": "Something wrong....",
                    "error": str(Err),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
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
                return Response(
                    {
                        "message": "Update Success.",
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "message": "Update Failed.",
                        "error": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Groups.DoesNotExist:
            return Response(
                {
                    "message": "Models Does not Found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    # +=========+=========+=========+=========+=========
    # DELETE(destroy)
    # +=========+=========+=========+=========+=========
    def destroy(self, request, pk=None):
        try:
            target = Groups.objects.get(id=pk)
            target.delete()
            return Response(
                {
                    "message": "Delete Success.",
                },
                status=status.HTTP_200_OK,
            )
        except Groups.DoesNotExist:
            return Response(
                {
                    "message": "Models Does not Found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# =========+=========+=========+=========+=========+


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.none()
    serializer_class = TaskSerializer

    # +=========+=========+=========+=========+=========
    # GET(list)
    # +=========+=========+=========+=========+=========
    def retrieve(self, request, pk=None):
        try:
            with transaction.atomic():
                # Get Task Data
                objs = Task.objects.filter(group_id=pk)
                obj_list = TaskSerializer(objs, many=True).data
                task_list = []
                if obj_list:
                    for task in obj_list:
                        task_id = task.get("id")
                        if task_id is not None:
                            # Get Posting Data
                            post_data = PostsSerializer(
                                Posts.objects.get(task_id=task_id)
                            ).data

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
                                "task": task,
                                "post": post_data,
                                "prompt": prompt_data,
                                "request": request_data,
                            }
                        else:
                            data = {
                                "task": task,
                                "post": None,
                                "prompt": None,
                                "request": None,
                            }

                        task_list.append(data)
                    return Response(
                        {
                            "data": task_list,
                        },
                        status=status.HTTP_200_OK,
                    )

        except Exception as Err:
            return Response(
                {
                    "message": "Something wrong....",
                    "error": str(Err),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# =========+=========+=========+=========+=========+


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.none()
    serializer_class = PostsSerializer

    def create(self, request, pk=None):
        req_data = request.data
        serializer = PostsSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Update Success.",
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "message": "Add Failed.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def partial_update(self, request, pk=None):
        req_data = request.data
        try:
            target = Posts.objects.get(task_id=pk)
            serializer = PostsSerializer(target, data=req_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Update Success.",
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "message": "Update Failed.",
                        "error": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as Err:
            return Response(
                {
                    "message": "Something wrong....",
                    "error": str(Err),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# =========+=========+=========+=========+=========+


class PromptsViewSet(viewsets.ModelViewSet):
    queryset = Prompts.objects.none()
    serializer_class = PromptsSerializer

    def create(self, request, pk=None):
        req_data = request.data
        serializer = PromptsSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Add Success.",
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "message": "Add Failed.",
                    "error": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def partial_update(self, request, pk=None):
        req_data = request.data
        try:
            target = Prompts.objects.get(task_id=pk)
            serializer = PromptsSerializer(target, data=req_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Update Success.",
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "message": "Add Failed.",
                        "error": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as Err:
            return Response(
                {
                    "message": "Something wrong....",
                    "error": str(Err),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# =========+=========+=========+=========+=========+


class RequestsViewSet(viewsets.ModelViewSet):
    queryset = Requests.objects.none()
    serializer_class = RequestsSerializer

    def create(self, request, pk=None):
        req_data = request.data
        try:
            with transaction.atomic():
                for key, item in req_data.items():
                    match key:
                        case "basis":
                            serializer = BasisSerializer(data=item)
                        case "location":
                            serializer = LocationSerializer(data=item)
                        case "outfits":
                            serializer = OutfitsSerializer(data=item)
                        case "hairs":
                            serializer = HairsSerializer(data=item)
                        case "faces":
                            serializer = FacesSerializer(data=item)
                        case "figures":
                            serializer = FiguresSerializer(data=item)
                        case "uppers":
                            serializer = UppersSerializer(data=item)
                        case "lowers":
                            serializer = LowersSerializer(data=item)
                        case "colors":
                            serializer = ColorsSerializer(data=item)
                        case _:
                            return Response(
                                {
                                    "message": "Add Failed.",
                                    "error": f"[{key}]Model is not Found",
                                },
                                status=status.HTTP_404_NOT_FOUND,
                            )

                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(
                            {
                                "message": "Add Failed.",
                                "error": serializer.errors,
                            },
                            status=status.HTTP_400_BAD_REQUEST,
                        )
        except Exception as Err:
            return Response(
                {
                    "message": "Something wrong....",
                    "error": str(Err),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(
            {
                "message": "Add Success.",
            },
            status=status.HTTP_200_OK,
        )

    def partial_update(self, request, pk=None):
        req_data = request.data
        try:
            with transaction.atomic():
                for key, item in req_data.items():
                    match key:
                        case "basis":
                            target = Basis.objects.get(task_id=pk)
                            serializer = BasisSerializer(
                                target, data=item, partial=True
                            )
                        case "location":
                            target = Location.objects.get(task_id=pk)
                            serializer = LocationSerializer(
                                target, data=item, partial=True
                            )
                        case "outfits":
                            target = Outfits.objects.get(task_id=pk)
                            serializer = OutfitsSerializer(
                                target, data=item, partial=True
                            )
                        case "hairs":
                            target = Hairs.objects.get(task_id=pk)
                            serializer = HairsSerializer(
                                target, data=item, partial=True
                            )
                        case "faces":
                            target = Faces.objects.get(task_id=pk)
                            serializer = FacesSerializer(
                                target, data=item, partial=True
                            )
                        case "figures":
                            target = Figures.objects.get(task_id=pk)
                            serializer = FiguresSerializer(
                                target, data=item, partial=True
                            )
                        case "uppers":
                            target = Uppers.objects.get(task_id=pk)
                            serializer = UppersSerializer(
                                target, data=item, partial=True
                            )
                        case "lowers":
                            target = Lowers.objects.get(task_id=pk)
                            serializer = LowersSerializer(
                                target, data=item, partial=True
                            )
                        case "colors":
                            target = Colors.objects.get(task_id=pk)
                            serializer = ColorsSerializer(
                                target, data=item, partial=True
                            )
                        case _:
                            return Response(
                                {
                                    "message": "Update Failed.",
                                    "error": f"[{key}]Model is not Found",
                                },
                                status=status.HTTP_404_NOT_FOUND,
                            )

                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(
                            {
                                "message": "Update Failed.",
                                "error": serializer.error,
                            },
                            status=status.HTTP_400_BAD_REQUEST,
                        )
        except Exception as Err:
            return Response(
                {
                    "message": "Something wrong....",
                    "error": str(Err),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(
            {
                "message": "Update Success.",
            },
            status=status.HTTP_200_OK,
        )


# =========+=========+=========+=========+=========+
