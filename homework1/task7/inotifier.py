from abc import ABC, abstractmethod


class INotifier(ABC):
    @abstractmethod
    def send(self, msg):
        pass
