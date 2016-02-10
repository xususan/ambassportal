from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse

import requests

def testRequest(request):
    headers = {
    "content-type": "application/vnd.api+json",
    "x-user-location": "[54,12]"
    }
    res = requests.get("https://masu-api-staging.sngp.co/ambassador/supervisors", headers=headers)
    # print(res.status_code, res.reason)
    return res

def anotherTest(request):
	    headers = {
    "content-type": "application/vnd.api+json",
    "x-user-location": "[54,12]"
    }
     res = requests.post("https://masu-api-staging.sngp.co/ambassador/supervisors", headers=headers, 
     	"data"= {
    "attributes": {
      "first_name": "aaa",
      "last_name": "bbb",
      "email":"test@test.com",
      "supervisor_id": "e9b73827-acb9-46d7-b330-527a679ce975",
      "college": "Harvard",
      "password": "p@ssw0rd"
    }
  }
)
    # print(res.status_code, res.reason)
    return res

def index(request):
    return HttpResponse(anotherTest(request).text)

#def index(request):
	#return render(request,'userprofile/index.html')