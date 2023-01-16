from django.db import models
from django.conf import settings
import uuid



class Profile(models.Model):
    class Meta:
        verbose_name_plural='プロファイル'

    user = models.OneToOneField(
             settings.AUTH_USER_MODEL,
             on_delete=models.CASCADE,
             related_name='%(app_label)s_%(class)s_user',
           )
    nick_name = models.CharField(
                  verbose_name='ニックネーム',
                  blank=True,
                  null=True,
                  max_length=200,
                )
    created_at = models.DateTimeField(
                   verbose_name='作成日時',
                   auto_now_add=True,
                 )
    updated_at = models.DateTimeField(
                   verbose_name='更新日時',
                   auto_now=True,
                 )

    def __int__(self):
        return self.nick_name


class Art(models.Model):
    class Meta:
        verbose_name_plural='アート'

    file_name = models.UUIDField(
            default=uuid.uuid4,
            editable=False
            )
    user = models.ForeignKey(
             settings.AUTH_USER_MODEL,
             on_delete = models.DO_NOTHING,
             related_name = '%(app_label)s_%(class)s_user',
           )
    prompt = models.CharField(
            verbose_name='prompt',
            max_length=400,
            )
    seed = models.PositiveIntegerField(
            verbose_name='seed',
            default=42,
            )
    scale = models.FloatField(
            verbose_name='scale',
            default=0.7,
            )
    ddim_steps = models.PositiveIntegerField(
                verbose_name='ddim_steps',
                default=50,
              )
    n_iter = models.PositiveIntegerField(
                verbose_name='n_iter',
                default=1,
              )
    is_generated = models.BooleanField(
            verbose_name='作成済',
            default=False,
            )
    created_at = models.DateTimeField(
                   verbose_name='作成日時',
                   auto_now_add=True,
                 )
    updated_at = models.DateTimeField(
                   verbose_name='更新日時',
                   auto_now=True,
                 )

    def __int__(self):
        return self.nick_name

