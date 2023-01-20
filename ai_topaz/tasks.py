from __future__ import absolute_import, unicode_literals

#from .celery import app
from celery import shared_task
from api.schemas import ArtIn
from api.models import Art
import subprocess

#デバッグ用 オブジェクト表示
import pprint


print('DEAD BEEF tasks 1')
#print(app.conf.broker_url)


#@app.task
@shared_task
def add(x, y):
    return x + y

import time

@shared_task
def txt2img_task(art_id):
    print('txt2img_task開始')

    #subprocess.run(f'/home/ishizuka/txt2img_v2.sh {filename} "{t2i.prompt}" {t2i.seed} {t2i.n_iter} {t2i.scale} {t2i.ddim_steps}', shell=True)
    #img = {'file': open(f"/home/ishizuka/stable-diffusion/outputs/txt2img-samples/{filename}-grid.png", 'rb')}

    time.sleep(1)
    print(f'txt2img_task依頼art_id: {art_id}')
    try:
        art = Art.objects.get(pk=art_id)
        pprint.pprint(f'art: {vars(art)}')
    except Art.DoesNotExist:
        print(f'Artレコードが無いよ！')

    # バリデーションしっかりしないとヤバい
    subprocess.run(f'/home/ishizuka/dev-txt2img.sh {art.file_name} "{art.prompt}" {art.seed} {art.n_iter} {art.scale} {art.ddim_steps}', shell=True)

    # ファイル保存場所はS3にしよう
    #img = {'file': open(f"/home/ishizuka/stable-diffusion/outputs/txt2img-samples/{art.file_name}-grid.png", 'rb')}

    #subprocess.run(f"rm /home/ishizuka/stable-diffusion/outputs/txt2img-samples/{art.file_name}-grid.png", shell=True)
    #subprocess.run(f"rm /home/ishizuka/stable-diffusion/outputs/txt2img-samples/samples/{art.file_name}*.png", shell=True)

    art.is_generated = True
    art.save()

    print('txt2img_task終了')

    #return f'DEAD BEEF OK!'


#@app.task
#def mul(x, y):
#    return x * y

#@app.task
#def xsum(numbers):
#    return sum(numbers)

