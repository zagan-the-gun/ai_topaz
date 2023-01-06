from ninja import NinjaAPI
from pydantic import BaseModel
from typing import Union
#from .tasks import add
from ai_topaz.tasks import add

api = NinjaAPI()


class T2I(BaseModel):
    prompt: Union[str, None] = "Daimyo's procession of 20cm in length that only I can see."
    seed: Union[int, None] = 42
    scale: Union[float, None] = 0.7
    ddim_steps: Union[int, None] = 50
    n_iter: Union[int, None] = 1

@api.post("/txt2img")
def txt2img(request, t2i: T2I):
    #res = add.delay(x, y)
    return "OK!"

@api.get("/get_test")
def get_test(request):
    return "get test!"

@api.get("/hello")
def hello(request, x:int=1 , y:int=1):
    #res = add(x, y)
    res = add.delay(x, y)
    #res = add.apply_async(x, y)
    #res = add.apply_async((x, y), queue='lopri', countdown=10)

    return f"hello {x, y, res}"

