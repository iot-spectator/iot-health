# Copyright © 2020 by IoT Spectator. All rights reserved.

"""Interface definition."""

import abc

from typing import List


class BaseHealth(abc.ABC):
    """Definition for common health information."""

    @classmethod
    @abc.abstractmethod
    def summary(cls) -> dict:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def device_platform(cls) -> str:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def processor_architecture(cls) -> str:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def operating_system(cls) -> str:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def processors(cls) -> List[dict]:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def memory(cls) -> dict:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def capacity(cls) -> dict:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def temperature(cls) -> float:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def cameras(cls) -> List[dict]:
        raise NotImplementedError()
