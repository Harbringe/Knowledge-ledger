from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db import connection
from django.core.cache import cache
import os

# Create your views here.

@csrf_exempt
@require_http_methods(["GET"])
def health_check(request):
    """
    Health check endpoint for Render monitoring
    """
    try:
        # Check database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"
    
    # Check cache
    try:
        cache.set("health_check", "ok", 10)
        cache_status = "healthy"
    except Exception as e:
        cache_status = f"unhealthy: {str(e)}"
    
    # Check environment
    env_status = "healthy"
    required_vars = ['SECRET_KEY', 'DB_CONN_URL']
    for var in required_vars:
        if not os.getenv(var):
            env_status = f"missing: {var}"
    
    overall_status = "healthy" if all([
        db_status == "healthy",
        cache_status == "healthy",
        env_status == "healthy"
    ]) else "unhealthy"
    
    return JsonResponse({
        "status": overall_status,
        "timestamp": os.getenv('RENDER_TIMESTAMP', 'unknown'),
        "service": os.getenv('RENDER_SERVICE_NAME', 'knowledge-ledger-backend'),
        "checks": {
            "database": db_status,
            "cache": cache_status,
            "environment": env_status
        }
    }, status=200 if overall_status == "healthy" else 503)
