import Logger


def runnableTask(task):
    """
    Wrapper function , wraps a task and prints additional logging information.

    :param: object task: The function object to wrap
    :rtype: object
    :return: The wrapped function object
    """
    def wrappedTask(*args, **kwargs):
        task_name = task.__name__
        Logger.logD('Executing task : ' + task_name)
        task(*args, **kwargs)
        Logger.logD('Finished task : ' + task_name)

    return wrappedTask