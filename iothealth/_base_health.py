# Copyright © 2020 by IoT Spectator. All rights reserved.

"""Interface definition."""

import abc

from typing import List


class BaseHealth(abc.ABC):
    """Definition for common health information."""

    @classmethod
    @abc.abstractmethod
    def summary(cls) -> dict:
        """Provide the device health summary."""
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def device_platform(cls) -> str:
        """Provide the device platform info."""
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def processor_architecture(cls) -> str:
        """Provide the device CPU info."""
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def operating_system(cls) -> str:
        """Provide the device OS info."""
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def processors(cls) -> List[dict]:
        """Provice the device processors info."""
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def memory(cls) -> dict:
        """Provide the device memory info."""
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def capacity(cls) -> dict:
        """Provide the device disk usage info."""
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def temperature(cls) -> float:
        """Provide the device temperature."""
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def cameras(cls) -> List[dict]:
        """Provide the cameras info."""
        raise NotImplementedError()
