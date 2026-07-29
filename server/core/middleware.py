# ponytail: read-only public search API, so a static allow-all beats pulling in django-cors-headers
def cors_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        return response

    return middleware
