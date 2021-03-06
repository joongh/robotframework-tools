# robotframework-tools
#
# Python Tools for Robot Framework and Test Libraries.
#
# Copyright (C) 2013-2016 Stefan Zimmermann <zimmermann.code@gmail.com>
#
# robotframework-tools is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# robotframework-tools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with robotframework-tools. If not, see <http://www.gnu.org/licenses/>.

"""robottools.library.inspector.arguments

.. moduleauthor:: Stefan Zimmermann <zimmermann.code@gmail.com>
"""
__all__ = ['KeywordArgumentsInspector']


class KeywordArgumentsInspector(object):
    def __init__(self, arguments):
        self._arguments = arguments

    def __getattr__(self, name):
        return getattr(self._arguments, name)

    def __dir__(self):
        return ['positional', 'defaults', 'varargs', 'kwargs']

    def __iter__(self):
        args = self._arguments
        for argname, defaults_index in zip(
          args.positional, range(-len(args.positional), 0)
          ):
            try:
                default = args.defaults[defaults_index]
            except IndexError:
                yield argname
            else:
                yield '%s=%s' % (argname, default)
        if args.varargs:
            yield '*' + args.varargs
        if args.kwargs:
            yield '**' + args.kwargs

    def __str__(self):
        return ' | '.join(self)

    def __repr__(self):
        return '[Arguments] %s' % self
