from celery import shared_task

@shared_task
def status_blog():
    print("blog is modified")
