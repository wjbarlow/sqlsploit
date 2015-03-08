import click


@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.option('--keyword', '-k', is_flag=True, help='Keyword for searching')
@click.option('--searchtype', '-t', type=click.Choice(['Default', 'Pattern', 'Smart', 'Keyword']))
@click.argument('name', default='world', required=False)
def main(name, as_cowboy):
    """SQL Data discovery tool."""
    greet = 'Howdy' if as_cowboy else 'Hello'
    click.echo('{0}, {1}.'.format(greet, name))
