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
        task(args)
        Logger.logD('Finished task : ' + taskName)

    return wrappedTask
