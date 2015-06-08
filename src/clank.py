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

    def do_quit(self, arg):
        """
        Quit the program.

        Quit Clank by returning `True`, which causes `self.cmdloop()` to exit.

        :returns: True
        :rtype: bool
        """
        return True

    def do_EOF(self, arg):
        """
        Handle EOF input by quitting.

        Handle EOF input (passed as the string `'EOF'`) by exiting the shell's
        command loop.
        """
        self.do_quit(arg)

if __name__ == '__main__':
    Shell().cmdloop()
