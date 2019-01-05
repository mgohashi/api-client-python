# Sample Tornado Python API-Client

### To install it use
```shell
$ python3 setup.py install
```

### Available endpoints

| HTTP Method | URL                      | REQUEST BODY           | RESPONSE BODY                     |
|-------------|--------------------------|------------------------|-----------------------------------|
| GET         | /api/v1/client           |                        | Ref [Array Client](#array-client) |  
| POST        | /api/v1/client           |                        | Ref [Client](#client)             |
| GET         | /api/v1/client/([0-9]*)  |                        | Ref [Client](#client)             |
| PUT         | /api/v1/client/([0-9]*)  | Ref [Client](#client)  | Ref [Client](#client)             |
| DELETE      | /api/v1/client/([0-9]*)  |                        | Ref [Client](#client)             |

### Model

#### Array Client

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

#### Client
```javascript
{
	"oid": "string",
	"name": "string",
	"email": "string",
	"birth_date": "date"
}
```
