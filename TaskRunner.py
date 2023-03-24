import time

import Logger
from ConfigProvider import ConfigProvider


def runnableTask(task: callable) -> callable:
    """
    Wrapper function , wraps a task and prints additional logging information.

    Parameters:
    object task: The function object to wrap

    return type:
    object

    return:
    The wrapped function object
    """

    def wrappedTask() -> None:
        currentTaskName = task.__name__
        args = ConfigProvider.getBoolean(ConfigProvider.SECTION_TASKS, currentTaskName)
        Logger.logD('Executing task : ' + currentTaskName)
        startTime = time.perf_counter()
        task(args)
        taskTime = time.perf_counter() - startTime
        Logger.logD(f'Task : {currentTaskName} finished, took {taskTime:.4f} seconds')

    return wrappedTask
