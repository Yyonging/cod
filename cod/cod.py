import sys
import click

from prompt_toolkit import PromptSession
from prompt_toolkit import HTML
from prompt_toolkit import print_formatted_text as _print
from prompt_toolkit.completion import NestedCompleter

commands = {}
_buildin_commands = {}
command_completer = NestedCompleter({})
session = PromptSession()
tip = '>>>'

def main():
    while 1:
        try:
            user_input = session.prompt(tip, completer=command_completer, complete_while_typing=True)
            f_inputs = list(filter(lambda x: x != '', user_input.split(' ')))
            buildin_commands(f_inputs[0])
            func = commands.get(f_inputs[0], None)
            if func:
                try:func(f_inputs[1:])
                except SystemExit:pass
            else:
                _print(HTML(f'there is no <ansired>{f_inputs[0]}</ansired> command!'))
        except KeyboardInterrupt:
            _print(HTML(f'<ansired>exit!</ansired>'))
            sys.exit(1)

def echo(text):
    _print(HTML(f'<ansigreen>{str(text)}</ansigreen>'))

command = click.command

def register(name=None, cls=None, **attrs):
    def decorator(f):
        cmd = command(name, cls, **attrs)(f)
        commands[cmd.name] = cmd
        command_completer.options.update({cmd.name:None})
        return cmd
    return decorator

click.command = register

def exit():
    raise KeyboardInterrupt

def quit():
    raise KeyboardInterrupt

_buildin_commands.update({'exit':exit, 'quit':quit})
command_completer.options.update({'exit':None, 'quit':None})

def buildin_commands(cmd):
    if cmd in _buildin_commands:
        _buildin_commands[cmd]()
