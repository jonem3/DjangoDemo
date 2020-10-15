import hashlib

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from databasetables.models import Users
import json

@csrf_exempt
def signup(request):
    if request.method == "POST":
        print("Request Body", request.body.decode('utf-8'))
        print("Headers: ", request.headers)
        jason = json.loads(request.body.decode('utf-8'))
        print(jason)
        newUser = Users()
        newUser.userid = jason['user_id']
        newUser.username = jason['user_name']
        newUser.password = hashlib.sha512(str.encode(jason['password'])).hexdigest()
        newUser.save()
        returnJson = {"Saved": True}
        return JsonResponse(returnJson)


@csrf_exempt
def login(request):
    # Compares the request method
    if request.method == "POST":
        # Retrieve the JSON from the request and decode from binary format to UTF-8
        jason = json.loads(request.body.decode('utf-8'))

        """
        Example JASON:
        {user_id: 0,
        user_name: "User",
        password: "A_Password",
        }
        """

        # Retrieve row from database as an object. DO NOT USE THIS METHOD IN NEA
        loginUser = Users.objects.filter(username=jason['user_name'],
                                         userid=jason['user_id'],
                                         password=hashlib.sha512(str.encode(jason['password'])).hexdigest()).first()

        # If a user is found a JSON string containing a confirmation will be returned
        # Otherwise a negative will be returned
        if loginUser is not None:
            returnJson = {"UserFound": True,
                          "UserID": loginUser.userid,
                          "UserName": loginUser.username,
                          "Password": loginUser.password}
        else:
            returnJson={
                "UserFound": False
            }

        """
        if loginUser.findUserByUserID(jason['user_id'] != null:
            foundUser = True
            return User (Build Json as below)
        else:
            return User Not Found (Build Error Json)
        """



        # If User Not Found: UserFound should be False
        return JsonResponse(returnJson)

