from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'john',
            'age': 23
        }
        return Response(data)




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