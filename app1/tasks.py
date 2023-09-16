# Create your tasks here
import time

from proj.celery import app


@app.task
def test_task_a():
    print('test_task')

    for i in range(20):
        time.sleep(1)
        print(i, '秒')
    return 'test_task'
