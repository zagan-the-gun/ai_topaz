from django.contrib import admin
from .models import Profile, Art


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #list_editable   = ['application']
    list_filter     = ['created_at', 'updated_at',]
    search_fields   = ['user__username', 'nick_name',]
    list_display    = ['user', 'nick_name', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    fields          = ['user', 'nick_name', 'created_at', 'updated_at']
    #登録時にオートコンプリートで探せる
    #autocomplete_fields = ['application']

@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    #list_editable   = ['application']
    list_filter     = ['file_name', 'user', 'prompt', 'seed', 'scale', 'ddim_steps', 'n_iter', 'is_generated', 'created_at', 'updated_at',]
    search_fields   = ['file_name', 'user__username', 'prompt',]
    list_display    = ['file_name', 'user', 'prompt', 'seed', 'scale', 'ddim_steps', 'n_iter', 'is_generated', 'created_at', 'updated_at']
    readonly_fields = ['file_name', 'user', 'prompt', 'seed', 'scale', 'ddim_steps', 'n_iter', 'is_generated', 'created_at', 'updated_at']
    fields          = ['file_name', 'user', 'prompt', 'seed', 'scale', 'ddim_steps', 'n_iter', 'is_generated', 'created_at', 'updated_at']
    #登録時にオートコンプリートで探せる
    #autocomplete_fields = ['file_name', 'prompt',]

