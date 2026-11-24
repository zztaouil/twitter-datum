from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.utils.cache import patch_vary_headers


def cors_middleware(get_response):
    def middleware(request):
        allowed_origin = getattr(settings, "DATUM_WEB_ORIGIN", None)
        origin = request.headers.get("Origin")
        if allowed_origin and request.method in {"POST", "DELETE"} and origin != allowed_origin:
            return HttpResponseForbidden()

        response = HttpResponse() if request.method == "OPTIONS" else get_response(request)
        if allowed_origin:
            patch_vary_headers(response, ("Origin",))
        if not allowed_origin or origin == allowed_origin:
            response["Access-Control-Allow-Origin"] = allowed_origin or "*"
            response["Access-Control-Allow-Methods"] = "GET, POST, DELETE, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    return middleware
