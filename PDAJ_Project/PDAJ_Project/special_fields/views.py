from django.shortcuts import render
from rest_framework.views import APIView
import json
import time
import tracemalloc
from django.http import HttpResponse
from .solutions.seq import main as mainSeq
from .solutions.comperhension import main as mainComp
from .solutions.generators import main as mainGen
from .solutions.par import main as mainPar

class SeqApi(APIView):

    def post(self,request):
        return MainSeq(request)

def MainSeq(request):
    n, m, special_fields = getParams(request.data)

    tracemalloc.start()
    start_time = time.time()
    results = mainSeq(n, m ,special_fields)
    time_in_s = time.time() - start_time

    _, peak = tracemalloc.get_traced_memory()
    max_memory_in_MB = peak / 10**6

    data = getResponse(results, time_in_s, max_memory_in_MB)
    tracemalloc.stop()

    dump = json.dumps(data)
    return HttpResponse(dump,content_type='application/json')

class CompApi(APIView):
    def post(self,request):
        return MainComp(request)

def MainComp(request):
    n, m, special_fields = getParams(request.data)

    tracemalloc.start()
    start_time = time.time()
    results = mainComp(n, m, special_fields)
    time_in_s = time.time() - start_time

    _, peak = tracemalloc.get_traced_memory()
    max_memory_in_MB = peak / 10**6

    data = getResponse(results, time_in_s, max_memory_in_MB)
    tracemalloc.stop()

    dump = json.dumps(data)
    return HttpResponse(dump,content_type='application/json')

class GenApi(APIView):
    def post(self,request):
        return MainGen(request)

def MainGen(request):
    n, m, special_fields = getParams(request.data)

    tracemalloc.start()
    start_time = time.time()
    results = mainGen(n, m, special_fields)
    time_in_s = time.time() - start_time

    _, peak = tracemalloc.get_traced_memory()
    max_memory_in_MB = peak / 10**6

    data = getResponse(results, time_in_s, max_memory_in_MB)
    tracemalloc.stop()

    dump = json.dumps(data)
    return HttpResponse(dump,content_type='application/json')

class ParApi(APIView):
    def post(self,request):
        return MainPar(request)

def MainPar(request):
    n, m, special_fields = getParams(request.data)

    tracemalloc.start()
    start_time = time.time()
    results = mainPar(special_fields, n, m)
    time_in_s = time.time() - start_time

    _, peak = tracemalloc.get_traced_memory()
    max_memory_in_MB = peak / 10**6

    data = getResponse(results, time_in_s, max_memory_in_MB)
    tracemalloc.stop()

    dump = json.dumps(data)
    return HttpResponse(dump,content_type='application/json')

def getResponse (result, time_in_s, max_memory_in_MB):
    data = {
        'result': result,
        'time_in_s': time_in_s,
        'max_memory_in_MB': max_memory_in_MB
    }
    return data

def getParams(data):
    n = int(data["n"])
    m = int(data["m"])
    special_fields = data["points"]
    return n, m, special_fields