# Copyright © 2020 by IoT Spectator. All rights reserved.

"""General Linux health info on x86 platform."""

import platform
import shutil
import subprocess

import psutil

from typing import List

from iothealth import _base_health


class Linux(_base_health.BaseHealth):
    """Health information for general Linux devices."""

    # Override
    @classmethod
    def summary(cls) -> dict:
        raise NotImplementedError()

    # Override
    @classmethod
    def device_platform(cls) -> str:
        """Get the system information.

        Returns
        -------
        `str`
            An empty string is returned if the platform is unknown.
            Otherwise, return the device platform info.
        """
        result = subprocess.run(
            ["cat", "/proc/version"], capture_output=True, text=True
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
            unknown. Otherwise, return the processor type, e.g., `x86_64`.
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
        raise NotImplementedError()

    # Override
    @classmethod
    def cameras(cls) -> List[dict]:
        raise NotImplementedError()
