# Copyright © 2020 by IoT Spectator. All rights reserved.

"""IoT Health CLI."""

import click

from iothealth import device_health


@click.group()
def cli():
    pass


@click.command()
def summary():
    click.echo(device_health.DeviceHealth().summary())


@click.command()
def platform():
    click.echo(device_health.DeviceHealth().device_platform())


@click.command()
def processor_arch():
    click.echo(device_health.DeviceHealth().processor_architecture())


@click.command()
def os_info():
    click.echo(device_health.DeviceHealth().operating_system())


@click.command()
def processors():
    click.echo(device_health.DeviceHealth().processors())


@click.command()
def memory():
    click.echo(device_health.DeviceHealth().memory())


@click.command()
def capacity():
    click.echo(device_health.DeviceHealth().capacity())


@click.command()
def temperature():
    click.echo(device_health.DeviceHealth().temperature())


@click.command()
def cameras():
    click.echo(device_health.DeviceHealth().cameras())


cli.add_command(summary)
cli.add_command(platform)
cli.add_command(processor_arch)
cli.add_command(os_info)
cli.add_command(processors)
cli.add_command(memory)
cli.add_command(capacity)
cli.add_command(temperature)
cli.add_command(cameras)


def main():
    cli()
