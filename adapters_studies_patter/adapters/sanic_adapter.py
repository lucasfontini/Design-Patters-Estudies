# adapters/sanic_adapter.py

class SanicRequestAdapter:

    def __init__(self, request):
        self.request = request

    def to_dict(self):
        return {
            "method": self.request.method,
            "path": self.request.path,
            "headers": dict(self.request.headers),
            "query": dict(self.request.args),
            "body": self.request.json,
        }