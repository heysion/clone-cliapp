# Copyright (C) 2013  Lars Wirzenius
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


'''Simplistic text re-formatter.

This module format text, paragraph by paragraph, so it is somewhat
nice-looking, with no line too long, and short lines joined. In
other words, like what the textwrap library does. However, it
extends textwrap by recognising bulleted lists.

'''


import textwrap


class TextFormat(object):

    def __init__(self, width=78):
        self._width = width

    def format(self, text):
        '''Return input string, but formatted nicely.'''

        filled_paras = []
        for para in self._paragraphs(text):
            filled_paras.append(self._format_paragraph(para))
        return '\n\n'.join(filled_paras)

    def _paragraphs(self, text):
        return text.split('\n\n')

    def _format_paragraph(self, paragraph):
        filled = textwrap.fill(paragraph, width=self._width)
        if paragraph.endswith('\n') and not filled.endswith('\n'):
            filled += '\n'
        return filled

