from abc import ABC, abstractmethod
from typing import Any

class Observer(ABC):
    @abstractmethod
    def update(self, event: str, data: Any):
        pass

class LoggingObserver(Observer):
    def update(self, event: str, data: Any):
        print(f"[LOG] Event: {event} - {data}")