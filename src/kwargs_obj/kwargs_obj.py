#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================


# Functions & classes =========================================================
class KwargsObj(object):
    """
    This class defines method to map kwargs to attributes, so you can just
    call :meth:`_kwargs_to_attributes` in your ``__init__``.

    There is also modified :meth:`__setattr__`` method, which disables to set
    new attributes. This may be good for preventing typos for data containers.
    """
    def __setattr__(self, name, value):
        """
        Disable setting values which are not defined in ``.__init__()``.
        """
        if hasattr(self, "_all_set") and name not in self.__dict__:
            raise ValueError("%s is not defined in this class!" % name)

        self.__dict__[name] = value

    def _kwargs_to_attributes(self, kwargs):
        """
        Put keys from `kwargs` to `self`, if the keys are already there.
        """
        for key, val in kwargs.iteritems():
            if key not in self.__dict__:
                raise ValueError(
                    "Can't set %s parameter - it is not defined here!" % key
                )

            self.__dict__[key] = val
