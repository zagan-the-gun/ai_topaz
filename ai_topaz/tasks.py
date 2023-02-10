from __future__ import absolute_import, unicode_literals

from celery import shared_task
from api.schemas import ArtIn
from api.models import Art
import subprocess

#デバッグ用 オブジェクト表示
import pprint


@shared_task
def add(x, y):
    return x + y


@shared_task
def txt2img_task(art_id):
    print('txt2img_task開始')

    print(f'txt2img_task依頼art_id: {art_id}')
    try:
        art = Art.objects.get(pk=art_id)
        pprint.pprint(f'art: {vars(art)}')
    except Art.DoesNotExist:
        print(f'Artレコードが無いよ！')

    # バリデーションしっかりしないとヤバい
    subprocess.run(f'/home/ishizuka/dev-txt2img.sh {art.file_name} "{art.prompt}" {art.seed} {art.n_iter} {art.scale} {art.ddim_steps}', shell=True)

    art.is_generated = True
    art.save()

    print('txt2img_task終了')

