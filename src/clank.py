# Clank Main Shell
# Author: Steve Matsumoto
# This code is released under the GNU LGPL Version 3.

"""
:mod:`clank` --- Main Clank Shell
=================================
"""

import cmd

class Shell(cmd.Cmd):
    """
    Command-line interface to receive and process user commands.
    """

    intro = 'Clank Version 0.1 - Steve Matsumoto\n'
    prompt = 'clank > '

    def do_EOF(self, arg):
        """
        Handler for EOF input.
        """
        return True

if __name__ == '__main__':
    Shell().cmdloop()
