why? 
adapta interfaces diferentes para um mesmo formato.


Flask --->          adapter1 -----> Business rules 
Other Frame ---->   adapter2 -----> Business rules
other imple ---->   new adapter ----> Business rules

open to add 
close to modify

how to use? 

maintain the business rules without changes if framework needed to change


project/
│
├── adapters/
│   ├── flask_adapter.py
│   └── sanic_adapter.py
│
├── app_flask.py
└── app_sanic.py
