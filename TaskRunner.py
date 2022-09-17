import time

import ConfigProvider
import Globals
import Logger


def runnableTask(task):
    """
    Wrapper function , wraps a task and prints additional logging information.

    Parameters:
    object task: The function object to wrap

    return type:
    object

    return:
    The wrapped function object
    """
    def wrappedTask():

        taskName = task.__name__
        args = ConfigProvider.getBoolean(Globals.Config.SECTION_TASKS, taskName)
        Logger.logD('Executing task : ' + taskName)
        startTime = time.perf_counter()
        task(args)
        taskTime = time.perf_counter() - startTime
        Logger.logD(f'Task : {taskName} finished, took {taskTime:.4f} seconds')

    return wrappedTask
