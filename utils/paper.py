class Paper(object):
    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)


__all__ = ["Paper"]