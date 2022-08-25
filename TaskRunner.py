import Globals
import Logger
import InputUtils


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
    def wrappedTask(*args, **kwargs):

        task_name = task.__name__
        print(task.__doc__)
        userInput = InputUtils.getSafeInputFromUser()
        if userInput == "exit":
            exit(0)
        else:
            userInput = InputUtils.stringToBoolean(userInput)
        kwargs['userInput'] = userInput
        Logger.logD('Executing task : ' + task_name)
        task(*args, **kwargs)
        Logger.logD('Finished task : ' + task_name)

    return wrappedTask
