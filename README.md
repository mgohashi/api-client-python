# Sample Tornado Python API-Client

To configure use
```shell
$ export PIPENV_VENV_IN_PROJECT="1"
```
```shell
$ pipenv shell --fancy
```
```shell
$ pipenv install -e .
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
