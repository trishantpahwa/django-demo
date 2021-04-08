from django.http import JsonResponse
import redis
from django.conf import settings

redis = redis.Redis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


def users_(req, id):
    if req.method == 'GET':        
        a = redis.get("id-" + str(id))
        if a is not None:
            return JsonResponse({'Success': a.decode("utf-8")})
        else:
            return JsonResponse({'Success': False}) 
    if req.method == 'POST':
        
        return JsonResponse({'Success': True}, 201)
