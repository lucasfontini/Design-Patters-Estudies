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
        print("configura equipamento juniper", command)

#Below main code you can use these strategies

class Configure_device:
    def __init__(self, strategy):
        self.strategy = strategy

    def executar(self, command):
        self.strategy.configure(command)


#how to use
cisco = CiscoStrategy()
juniper = JuniperStrategy()
device = Configure_device(juniper)

print(device.executar("show version"))
