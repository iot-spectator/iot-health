# Copyright © 2020 by IoT Spectator. All rights reserved.

"""IoT Health."""

from typing import List, Optional

from iothealth import _base_health
from iothealth import linux
from iothealth import raspberry_pi


class DeviceHealth(_base_health.BaseHealth):

    _current_device_cache: Optional[_base_health.BaseHealth] = None

    # Override
    @classmethod
    def summary(cls) -> dict:
        """Provide the health information for the current device.

        Returns
        -------
        `dict`
            All the available health information as a key-value dictionary.
        """
        return DeviceHealth._current_device().summary()

    # Override
    @classmethod
    def device_platform(cls) -> str:
        return DeviceHealth._current_device().device_platform()

    # Override
    @classmethod
    def processor_architecture(cls) -> str:
        return DeviceHealth._current_device().processor_architecture()

    # Override
    @classmethod
    def operating_system(cls) -> str:
        return DeviceHealth._current_device().operating_system()

    # Override
    @classmethod
    def processors(cls) -> List[dict]:
        return DeviceHealth._current_device().processors()

    # Override
    @classmethod
    def memory(cls) -> dict:
        return DeviceHealth._current_device().memory()

    # Override
    @classmethod
    def capacity(cls) -> dict:
        return DeviceHealth._current_device().capacity()

    # Override
    @classmethod
    def temperature(cls) -> float:
        return DeviceHealth._current_device().temperature()

    # Override
    @classmethod
    def cameras(cls) -> List[dict]:
        return DeviceHealth._current_device().cameras()

    @classmethod
    def _current_device(cls) -> _base_health.BaseHealth:
        if cls._current_device_cache is None:
            if raspberry_pi.RaspberryPi().device_platform():
                cls._current_device_cache = raspberry_pi.RaspberryPi()
            else:
                cls._current_device_cache = linux.Linux()
        return cls._current_device_cache
