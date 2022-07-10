def enough(cap: int, on: int, wait: int):
    """
    Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. With so
    many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on
    the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.
    :param cap: the amount of people the bus can hold excluding the driver.
    :param on: the number of people on the bus excluding the driver.
    :param wait: the number of people waiting to get on to the bus excluding the driver.
    :return: 0 if there is enough space, else the number of passengers he can't take
    """
    return 0 if on + wait <= cap else abs(cap - (on + wait))
