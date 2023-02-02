from ninja import NinjaAPI
from pydantic import BaseModel
from typing import Union
#from .tasks import add
from ai_topaz.tasks import add, txt2img_task
from .schemas import ArtIn
from .models import Art
from django.contrib.auth.models import User
from django.http.response import JsonResponse


api = NinjaAPI()


class T2I(BaseModel):
    prompt: Union[str, None] = "Daimyo's procession of 20cm in length that only I can see."
    seed: Union[int, None] = 42
    scale: Union[float, None] = 0.7
    ddim_steps: Union[int, None] = 50
    n_iter: Union[int, None] = 1

@api.post("/txt2img")
def txt2img(request, art: ArtIn):
#def txt2img(request, t2i: T2I):
    #res = add.delay(x, y)
    #res = txt2img_task(art, 'DEAD_BEEF')
    #print(f'{res}')
    #txt2img_task(art, 'DEAD_BEEF')

    user = User.objects.get(pk=1)
    #art = Art.objects.create(user=user, prompt='', seed='', scale='', ddim_steps='', n_iter='')
    art = Art.objects.create(user=user, prompt=art.prompt, seed=art.seed, scale=art.scale, ddim_steps=art.ddim_steps, n_iter=art.n_iter)

    txt2img_task.delay(art.id)
    # 再起動面倒なので開発中は直接動かす
    #txt2img_task(art.id)

    print(f'{art.file_name}')
    return JsonResponse({"filename": art.file_name})

@api.get("/img/{file_name}")
async def get_img(file_name, response: Response):
    print(file_name)
    is_file = os.path.isfile(f"/home/ishizuka/stable-diffusion/outputs/txt2img-samples/{file_name}.png")
    if is_file:
        return FileResponse(f"/home/ishizuka/stable-diffusion/outputs/txt2img-samples/{file_name}.png")
    else:
        response.status_code = status.HTTP_202_ACCEPTED
        return

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

