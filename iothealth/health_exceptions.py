# Copyright © 2020 by IoT Spectator. All rights reserved.

"""Exception definitions for IoT health."""


class TemperatureError(Exception):
    """Raised when not able to retrieve device's temperature."""

    def __init__(self) -> None:
        Exception.__init__(self, "Temperature info is not available.")
