
import Logger
import TextUtils


def runnable_task(task):
    def wrapped_task(*args, **kwargs):
        task_name = TextUtils.to_camel_case(task.__name__)
        Logger.log_d('Executing task : ' + task_name)
        task(*args, **kwargs)
        Logger.log_d('Finished task : ' + task_name)
    return wrapped_task
