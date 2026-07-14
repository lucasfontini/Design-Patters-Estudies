from sanic import Sanic
from sanic.response import json

from adapters.sanic_adapter import SanicRequestAdapter

app = Sanic("app")

@app.post("/users")
async def users(request):

    req = SanicRequestAdapter(request).to_dict()
    
    # to_dict it return`s regardless of adapter same output data
    
    print(req)

    return json({
        "framework": "Sanic",
        "request": req
    })

app.run()