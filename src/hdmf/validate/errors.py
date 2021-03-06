
from ..utils import docval, getargs
from ..spec.spec import DtypeHelper
from numpy import dtype


__all__ = [
    "Error",
    "DtypeError",
    "MissingError",
    "ExpectedArrayError",
    "ShapeError",
    "MissingDataType",
    "IllegalLinkError",
    "IncorrectDataType"
]


class Error(object):

    @docval({'name': 'name', 'type': str, 'doc': 'the name of the component that is erroneous'},
            {'name': 'reason', 'type': str, 'doc': 'the reason for the error'},
            {'name': 'location', 'type': str, 'doc': 'the location of the error', 'default': None})
    def __init__(self, **kwargs):
        self.__name = getargs('name', kwargs)
        self.__reason = getargs('reason', kwargs)
        self.__location = getargs('location', kwargs)
        if self.__location is not None:
            self.__str = "%s (%s): %s" % (self.__name, self.__location, self.__reason)
        else:
            self.__str = "%s: %s" % (self.name, self.reason)

    @property
    def name(self):
        return self.__name

    @property
    def reason(self):
        return self.__reason

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, loc):
        self.__location = loc
        self.__str = "%s (%s): %s" % (self.__name, self.__location, self.__reason)

    def __str__(self):
        return self.__str

    def __repr__(self):
        return self.__str__()


class DtypeError(Error):

    @docval({'name': 'name', 'type': str, 'doc': 'the name of the component that is erroneous'},
            {'name': 'expected', 'type': (dtype, type, str, list), 'doc': 'the expected dtype'},
            {'name': 'received', 'type': (dtype, type, str, list), 'doc': 'the received dtype'},
            {'name': 'location', 'type': str, 'doc': 'the location of the error', 'default': None})
    def __init__(self, **kwargs):
        name = getargs('name', kwargs)
        expected = getargs('expected', kwargs)
        received = getargs('received', kwargs)
        if isinstance(expected, list):
            expected = DtypeHelper.simplify_cpd_type(expected)
        reason = "incorrect type - expected '%s', got '%s'" % (expected, received)
        loc = getargs('location', kwargs)
        super(DtypeError, self).__init__(name, reason, location=loc)


class MissingError(Error):
    @docval({'name': 'name', 'type': str, 'doc': 'the name of the component that is erroneous'},
            {'name': 'location', 'type': str, 'doc': 'the location of the error', 'default': None})
    def __init__(self, **kwargs):
        name = getargs('name', kwargs)
        reason = "argument missing"
        loc = getargs('location', kwargs)
        super(MissingError, self).__init__(name, reason, location=loc)


class MissingDataType(Error):
    @docval({'name': 'name', 'type': str, 'doc': 'the name of the component that is erroneous'},
            {'name': 'data_type', 'type': str, 'doc': 'the missing data type'},
            {'name': 'location', 'type': str, 'doc': 'the location of the error', 'default': None})
    def __init__(self, **kwargs):
        name, data_type = getargs('name', 'data_type', kwargs)
        self.__data_type = data_type
        reason = "missing data type %s" % self.__data_type
        loc = getargs('location', kwargs)
        super(MissingDataType, self).__init__(name, reason, location=loc)

    @property
    def data_type(self):
        return self.__data_type


class ExpectedArrayError(Error):

    @docval({'name': 'name', 'type': str, 'doc': 'the name of the component that is erroneous'},
            {'name': 'expected', 'type': (tuple, list), 'doc': 'the expected shape'},
            {'name': 'received', 'type': str, 'doc': 'the received data'},
            {'name': 'location', 'type': str, 'doc': 'the location of the error', 'default': None})
    def __init__(self, **kwargs):
        name = getargs('name', kwargs)
        expected = getargs('expected', kwargs)
        received = getargs('received', kwargs)
        reason = "incorrect shape - expected an array of shape '%s', got non-array data '%s'" % (expected, received)
        loc = getargs('location', kwargs)
        super(ExpectedArrayError, self).__init__(name, reason, location=loc)


class ShapeError(Error):

    @docval({'name': 'name', 'type': str, 'doc': 'the name of the component that is erroneous'},
            {'name': 'expected', 'type': (tuple, list), 'doc': 'the expected shape'},
            {'name': 'received', 'type': (tuple, list), 'doc': 'the received shape'},
            {'name': 'location', 'type': str, 'doc': 'the location of the error', 'default': None})
    def __init__(self, **kwargs):
        name = getargs('name', kwargs)
        expected = getargs('expected', kwargs)
        received = getargs('received', kwargs)
        reason = "incorrect shape - expected '%s', got '%s'" % (expected, received)
        loc = getargs('location', kwargs)
        super(ShapeError, self).__init__(name, reason, location=loc)


class IllegalLinkError(Error):
    """
    A validation error for indicating that a link was used where an actual object
    (i.e. a dataset or a group) must be used
    """

    @docval({'name': 'name', 'type': str, 'doc': 'the name of the component that is erroneous'},
            {'name': 'location', 'type': str, 'doc': 'the location of the error', 'default': None})
    def __init__(self, **kwargs):
        name = getargs('name', kwargs)
        reason = "illegal use of link"
        loc = getargs('location', kwargs)
        super(IllegalLinkError, self).__init__(name, reason, location=loc)


class IncorrectDataType(Error):
    """
    A validation error for indicating that the incorrect data_type (not dtype) was used.
    """

    @docval({'name': 'name', 'type': str, 'doc': 'the name of the component that is erroneous'},
            {'name': 'expected', 'type': str, 'doc': 'the expected data_type'},
            {'name': 'received', 'type': str, 'doc': 'the received data_type'},
            {'name': 'location', 'type': str, 'doc': 'the location of the error', 'default': None})
    def __init__(self, **kwargs):
        name = getargs('name', kwargs)
        expected = getargs('expected', kwargs)
        received = getargs('received', kwargs)
        reason = "incorrect data_type - expected '%s', got '%s'" % (expected, received)
        loc = getargs('location', kwargs)
        super(DtypeError, self).__init__(name, reason, location=loc)
