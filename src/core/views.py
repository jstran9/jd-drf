from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post





class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        # for one post (instance)
        # post = qs.first()
        # serializer = PostSerializer(post)
        # many must be specified as there are many instances.
        serializer = PostSerializer(qs, many=True)
        # data = {
        #     'name': 'john',
        #     'age': 23
        # }
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # passing in data into a serializer will also perform validation.
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




# Create your views here.
# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 23
#     }
#     # if we want to pass in a list or other data types
#     # we use the safe argument and set it to false.
#     # return JsonResponse(data, safe=False)
#     return JsonResponse(data, safe=False)