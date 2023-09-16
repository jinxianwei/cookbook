# Create your views here.
from django.http import JsonResponse

from app1.tasks import test_task_a


def test_task(request):  # Get, 提交task_id，返回任务状态，success
    if request.method == 'POST':
        task = {}
        result = test_task_a.delay()
        task_id = result.id
        task['task_id'] = task_id
        return JsonResponse(task)
