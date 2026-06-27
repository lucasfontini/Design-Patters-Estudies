from abc import ABC, abstractmethod


class ConfigStrategy(ABC):
    @abstractmethod
    def configure(self, command):
        pass


class CiscoStrategy(ConfigStrategy):
    def configure(self, command):
        print("configura equipamento cisco", command)

class MikrotikStrategy(ConfigStrategy):
    def configure(self , command):
        print("configura equipamento mikrotik", command)

class JuniperStrategy:
    def configure(self, command):
        print("configurao equipamento juniper")


#factory 

class StrategyFactory:

    """
    factory using if not registry

    """
    @staticmethod
    def create(vendor):
        if vendor == "cisco":
            return CiscoStrategy()
        if vendor == "mikrotik":
            return MikrotikStrategy()
        if vendor == "junos":
            return JuniperStrategy()
 

 