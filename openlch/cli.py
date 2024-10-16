"""Defines the CLI for the OpenLCH project."""

import subprocess

import click


@click.group()
def cli():
    """OpenLCH CLI tool for interacting with MilkV boards."""
    pass


@cli.command()
@click.option("--ip", required=True, help="IP address of the MilkV board")
def ping(ip):
    """Ping the MilkV board at the specified IP address."""
    try:
        result = subprocess.run(["ping", "-c", "4", ip], capture_output=True, text=True, check=False)
        if result.returncode == 0:
            click.echo(f"Successfully pinged {ip}")
            click.echo(result.stdout)
        else:
            click.echo(f"Failed to ping {ip}")
            click.echo(result.stderr)
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    cli()
