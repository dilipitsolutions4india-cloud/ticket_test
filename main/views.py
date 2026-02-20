from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# views.py


@csrf_exempt
def print_request(request):
    if request.method == "POST" or "GET":
        try:
            # Raw body
            raw_body = request.body.decode("utf-8")
            print("Raw Body:", raw_body)

            # If JSON payload
            data = json.loads(raw_body)
            print("Parsed JSON:", data)

            return JsonResponse({
                "status": "success",
                "received_data": data
            })

        except json.JSONDecodeError:
            return JsonResponse({
                "status": "error",
                "message": "Invalid JSON"
            }, status=400)

    return JsonResponse({
        "status": "error",
        "message": "Only POST method allowed"
    }, status=405)