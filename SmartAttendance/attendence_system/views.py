from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Attendance
from datetime import datetime
import json


@csrf_exempt
def mark_attendance(request):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=405)

    try:
        data = json.loads(request.body)
        name = data.get("name")

        if not name:
            return JsonResponse({"error": "Name is required"}, status=400)

        now = datetime.now()

        attendance, created = Attendance.objects.get_or_create(
            name=name,
            date=now.date(),
            defaults={
                "time": now.time()
            }
        )

        if created:
            return JsonResponse({
                "message": "Attendance marked",
                "name": name
            })

        return JsonResponse({
            "message": "Attendance already marked today",
            "name": name
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
