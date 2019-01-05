#Sample Tornado Python API-Client

###To install it use
```shell
$ python3 setup.py install
```

###Available endpoints

| HTTP Method | URL                      | REQUEST BODY           | RESPONSE BODY                     |
|-------------|--------------------------|------------------------|-----------------------------------|
| GET         | /api/v1/client           |                        | Ref [Array Client](#Array Client) |  
| POST        | /api/v1/client           |                        | Ref [Client](#Client)             |
| GET         | /api/v1/client/([0-9]*)  |                        | Ref [Client](#Client)             |
| PUT         | /api/v1/client/([0-9]*)  | Ref [Client](#Client)  | Ref [Client](#Client)             |
| DELETE      | /api/v1/client/([0-9]*)  |                        | Ref [Client](#Client)             |

###Model

####Array Client

```javascript
[
    //<One or mode>
    {
        "oid": "string",
        "name": "string",
        "email": "string",
        "birth_date": "date"
    },
    //More 
]
```

####Client
```javascript
{
	"oid": "string",
	"name": "string",
	"email": "string",
	"birth_date": "date"
}
```