
import Logger
import TextUtils


def runnable_task(task: object) -> object:
    """
    Wrapper function , wraps a task and prints additional logging information.

    :param: object task: The function object to wrap
    :rtype: object
    :return: The wrapped function object
    """
    def wrapped_task(*args, **kwargs):
        task_name = TextUtils.to_camel_case(task.__name__)
        Logger.log_d('Executing task : ' + task_name)
        task(*args, **kwargs)
        Logger.log_d('Finished task : ' + task_name)

    return wrapped_task
