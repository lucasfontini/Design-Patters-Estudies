# adapters/flask_adapter.py

class FlaskRequestAdapter:

    def __init__(self, request):
        self.request = request

    def to_dict(self):
        return {
            "method": self.request.method,
            "path": self.request.path,
            "headers": dict(self.request.headers),
            "query": self.request.args.to_dict(),
            "body": self.request.get_json(silent=True),
        }