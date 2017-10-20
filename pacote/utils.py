import click

@click.command()
@click.option('--n', default=1)
def cli(n):
    """Example script."""
    click.echo('Outro grupo de comandos')
    if n>4:
    	click.echo('Massa, n e maior que 4')
