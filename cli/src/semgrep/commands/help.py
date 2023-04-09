from typing import NoReturn

import click

from semgrep.commands.wrapper import handle_command_errors
from semgrep.verbose_logging import getLogger

logger = getLogger(__name__)
    
@click.command()
@click.pass_context
@handle_command_errors
def help(ctx: click.Context) -> NoReturn:
    """
    Show help for semgrep
    """
    cli = ctx.parent.command
    click.echo(cli.get_help(click.Context(cli)))
    
    
