from django.http import HttpResponse


# ponytail: small public API (search + pin/unpin), so a static allow-all beats pulling in django-cors-headers
def cors_middleware(get_response):
    def middleware(request):
        response = HttpResponse() if request.method == "OPTIONS" else get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    return middleware
