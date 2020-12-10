# Copyright © 2020 by IoT Spectator. All rights reserved.

"""Raspberry Pi health information."""

import platform
import re
import shutil
import subprocess

import psutil

from typing import List

from iothealth import _base_health
from iothealth import health_exceptions


class RaspberryPi(_base_health.BaseHealth):
    """Check Raspberry Pi health and status."""

    # Override
    @classmethod
    def summary(cls) -> dict:
        raise NotImplementedError()

    # Override
    @classmethod
    def device_platform(cls) -> str:
        """Get the IoT device platform.

        Returns
        -------
        `str`
            An empty string is returned if the platform is unknown.
            Otherwise, return the device platform info, e.g.,
            `Raspberry Pi 3 Model B Plus Rev 1.3`.
        """
        result = subprocess.run(
            ["cat", "/sys/firmware/devicetree/base/model"],
            capture_output=True,
            text=True,
        )
        if result.stderr:
            return str()
        return result.stdout.strip()

    # Override
    @classmethod
    def processor_architecture(cls) -> str:
        """Get the processor architecture.

        Returns
        -------
        `str`
            An empty string is returned if the processor architecture is
            unknown. Otherwise, return the processor type, e.g., `armv7l`.
        """
        return platform.processor()

    # Override
    @classmethod
    def operating_system(cls) -> str:
        """Get the OS info.

        Returns
        -------
        `str`
            An empty string is returned if the OS is unknown.
            Otherwise, return the processor type, e.g., `Linux`.
        """
        return platform.system()

    # Override
    @classmethod
    def processors(cls) -> List[dict]:
        raise NotImplementedError()

    # Override
    @classmethod
    def memory(cls) -> dict:
        """Get virtual memory usage in bytes.

        Returns
        -------
        `dict`
            Usages returned as a `dictionary` with keys `total`, `available`,
            and `used`.
        """
        result = psutil.virtual_memory()
        return {
            "total": result.total,
            "available": result.available,
            "used": result.used,
        }

    # Override
    @classmethod
    def capacity(cls) -> dict:
        """Get the current disk capacity usage in bytes.

        Returns
        -------
        `dict`
            Usages returned as a `dictionary` with keys `total`, `available`,
            and `used`.
        """
        result = shutil.disk_usage("/")
        return {"total": result.total, "available": result.free, "used": result.used}

    # Override
    @classmethod
    def temperature(cls) -> float:
        """Get the device's temperature.

        Returns
        -------
        float
            The device temperature, e.g., 54.8.
            The temperature unit is Celsius.

        Raises
        ------
        `TemperatureError`
            Raised if the temperature info is not available.
        """
        result = subprocess.run(
            ["/opt/vc/bin/vcgencmd", "measure_temp"],
            capture_output=True,
            text=True,
        )
        if not result.stderr:
            temp = re.search("\\d+\\.\\d+", result.stdout)
            if temp:
                return float(temp.group(0))

        raise health_exceptions.TemperatureError()

    # Override
    @classmethod
    def cameras(cls) -> List[dict]:
        raise NotImplementedError()
