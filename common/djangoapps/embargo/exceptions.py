"""Exceptions for the embargo app."""


class InvalidAccessPoint(Exception):
    """The requested access point is not supported. """

    def __init__(self, access_point, *args, **kwargs):
        msg = (
            u"Access point '{access_point}' should be either 'enrollment' or 'courseware'"
        ).format(access_point=access_point)
        super(InvalidAccessPoint, self).__init__(msg)