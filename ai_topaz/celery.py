import os
from celery import Celery

print('\n\n\nDEAD BEEF celery:1')

#app = Celery('ai_topaz',
#            broker='redis://dev-topaz-redis-001.wzdkbs.0001.apne1.cache.amazonaws.com:6379/0',
#            #broker_url='redis://dev-topaz-redis-001.wzdkbs.0001.apne1.cache.amazonaws.com:6379/0',
#            #backend='rpc://dev-topaz-redis-001.wzdkbs.0001.apne1.cache.amazonaws.com:6379/0',
#            #backend_url='rpc://dev-topaz-redis-001.wzdkbs.0001.apne1.cache.amazonaws.com:6379/0',
#            #result_backend='rpc://dev-topaz-redis-001.wzdkbs.0001.apne1.cache.amazonaws.com:6379/0',
#            backend='redis://dev-topaz-redis-001.wzdkbs.0001.apne1.cache.amazonaws.com:6379/0',
#            include=['ai_topaz.tasks'])

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_topaz.settings')
app = Celery('ai_topaz')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

#print(f"DEAD BEEF celery.py app.conf.broker_url: {app.conf.broker_url}\n\n\n")

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()

