from django.shortcuts import render
from rest_framework.parsers import JSONParser,ParseError
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from .models import *
from django.shortcuts import render #Default
from django.http import *
from django.shortcuts import get_object_or_404 #get object(error) when object not exist
from rest_framework.views import APIView #API data
from rest_framework.response import Response #Successful 200 response
from rest_framework import status #send back status 
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from . serializers import *
from rest_framework import status
import json
import pdb

# Via This class will give data in the json format
class DataList(APIView):

    def get(self, request):
    	user_list=Users.objects.all()
    	serializer=UserSerializer(user_list,many=True)
    	input_dict = serializer.data
    	final_dict = json.loads(json.dumps(input_dict))
    	return JsonResponse({
    		"ok":"true",
        	"members":final_dict,
        })
    
    def post(self, request):
        pass

		