import click


@click.command()
@click.option('--host', '-h', default='127.0.0.1', required=True, help='Host/IP')
@click.option('--username', '-u',default='sa', required=False, help='Username')
@click.option('--password', '-p', default='', hide_input=True, prompt=True, required=False, help='Password')
@click.option('--dbtype', '-db', default='MSSQL', type=click.Choice(['MySQL', 'MSSQL', 'Oracle', 'PG']), required=False, help='DB Type')
@click.option('--keyword', '-k', default='password', required=False, help='Search Keyword')
@click.option('--searchtype', '-s', default='Default', type=click.Choice(['Default', 'Pattern', 'Smart', 'Keyword']), required=False, help='Search Type')
@click.option('--version', '-V', default='0.1.0', required=False, help='SQLSploit Version')
def main(host, username, password, dbtype, keyword, searchtype, version):
    """SQLSploit - Data Extraction Toolkit"""
    click.echo('Host: %s' % host)
    click.echo('Username: %s' % username)
    click.echo('Password: %s' % password)
    click.echo('dbtype: %s' % dbtype)
    click.echo('Keyword: %s' % keyword)
    click.echo('searchtype: %s' % searchtype)
    click.echo('Version: %s' % version)