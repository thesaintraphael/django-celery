# simple Django app with periodic task written in CELERY
I added commands that you have to run in file Commands.txt:

1. py manage.py runserver ---> Runnig server
2. celery -A djangoProject worker -l info --pool=solo  ---> Running celery worker
3. celery -A djangoProject beat -l INFO  ---> Running beat (broker)
Add piece of code below to pyhtin file ayncio.py. Path to it, if you using vitrualenv should be in this way:

C:\django\yt-django-celery-series-intro-install-run-task\venv\lib\site-packages\tornado\platform\asyncio.py

import sys  # should be already imported

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
Check the Commands.txt file.
