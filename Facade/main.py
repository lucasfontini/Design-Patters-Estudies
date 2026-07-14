class Device:

    def connect(self):
        print("Conectando...")

    def configure(self, commands):
        for cmd in commands:
            print(f"Configurando: {cmd}")

    def save(self):
        print("Salvando configuração")

    def disconnect(self):
        print("Desconectando...")

class NetworkFacade:

    def __init__(self, device):
        self.device = device

    def configure(self, commands):
        self.device.connect()
        self.device.configure(commands)
        self.device.save()
        self.device.disconnect()


device = Device()

network = NetworkFacade(device)

network.configure([
    "hostname R1",
    "interface Loopback0",
    "ip address 1.1.1.1 255.255.255.255"
])


