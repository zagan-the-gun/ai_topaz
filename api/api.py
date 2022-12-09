from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/get_test")
def hello(request):
    return "get test!"

@api.get("/hello")
def hello(request):
    return f"hello {name}"

