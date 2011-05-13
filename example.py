# Copyright 2011  Lars Wirzenius
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


'''Example for cliapp framework.

This implements an fgrep-like utility.

'''


import cliapp
import logging


class ExampleApp(cliapp.Application):

    '''A little fgrep-like tool.'''
    
    def add_settings(self):
        self.settings.add_string_list_setting(['pattern', 'e'], 
                                      'search for regular expression PATTERN',
                                      metavar='REGEXP')

    # We override process_inputs to be able to do something after the last
    # input line.
    def process_inputs(self, args):
        self.matches = 0
        cliapp.Application.process_inputs(self, args)
        self.output.write('There were %s matches.\n' % self.matches)

    def process_input_line(self, name, line):
        for pattern in self.settings['pattern']:
            if pattern in line:
                self.output.write('%s:%s: %s' % (name, self.lineno, line))
                self.matches += 1
                logging.debug('Match: %s line %d' % (name, self.lineno))
    
    
app = ExampleApp(version='0.1.2')
app.settings.config_files = ['example.conf']
app.run()

