"""
usage: git [--version] [--help]
           <command> [<args>...]
The most commonly used git commands are:
   start      Add file contents to the index
   attach     poop
See 'agent help <command>' for more information on a specific command.
"""
from subprocess import call

from docopt import docopt


def main():
    args = docopt(__doc__,
                  version='agent version 0.0.1',
                  options_first=True)
    print('global arguments:')
    print(args)
    print('command arguments:')

    argv = [args['<command>']] + args['<args>']
    if args['<command>'] in 'start attach'.split():
        pass
        exit(call(['python', 'agent_%s.py' % args['<command>']] + argv))
    elif args['<command>'] in ['help', None]:
        pass
        exit(call(['python', 'cli.py', '--help']))
    else:
        print("hihihi")
        exit("%r is not a cli.py command. See 'agent help'." % args['<command>'])


#
#
#            <command> [<args>...]
# options:
#    -h, --help
#
# The most commonly used agent commands are:
#    start        creates a new agent with a new identifier
#    attach       creates a new agent with an existing wallet identifier
#
# See 'agent help <command>' for more information on a specific command.