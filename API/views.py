from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.http import HttpResponse
from .models import UserRecord, Users, SubmitRecord
import json
from django.core import serializers


# Create your views here.

def get_record(request):
    records = UserRecord.objects.all();
    data = {}
    data['list'] = json.loads(serializers.serialize("json", records))
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json,charset=utf-8")


def get_user(request, id):
    user = Users.objects.filter(user_id=id);
    data = {}
    data['list'] = json.loads(serializers.serialize("json", user))
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json,charset=utf-8")


def search(request, id):
    records = SubmitRecord.objects.filter(user_id2=id)
    sets = set()
    for record in records:
        sets.add(record.record_id1)
    data = {}
    data['list'] = json.loads(serializers.serialize("json", sets))
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json,charset=utf-8")
