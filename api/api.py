from ninja import NinjaAPI
from pydantic import BaseModel
from typing import Union
from ai_topaz.tasks import add, txt2img_task
from .schemas import ArtIn
from .models import Art
from django.contrib.auth.models import User
from django.http.response import JsonResponse


api = NinjaAPI()


class T2I(BaseModel):
    prompt: Union[str, None] = "Daimyo's procession of 20cm in length that only I can see."
    seed: Union[int, None] = 42
    n_iter: Union[int, None] = 1
    scale: Union[float, None] = 0.7
    ddim_steps: Union[int, None] = 50

@api.post("/txt2img")
def txt2img(request, art: ArtIn):
    user = User.objects.get(pk=1)
    art = Art.objects.create(user=user, prompt=art.prompt, seed=art.seed, n_iter=art.n_iter, scale=art.scale, ddim_steps=art.ddim_steps, )

    txt2img_task.delay(art.id)
    # celeryの再起動面倒なので開発中は直接動かす
    #txt2img_task(art.id)

    print(f'{art.file_name}')
    return JsonResponse({"filename": art.file_name})

@api.get("/get_test")
def get_test(request):
    return "get test!"

