# updock

a file host

## requirements

- Python 3
- A web host

## installation

- `python setup.py`
- http://flask.pocoo.org/docs/1.0/tutorial/deploy/

## usage

### upload file

```http
POST /create HTTP/1.1
Host: nice.website
Content-Type: multipart/form-data; boundary=X-FORM-BOUNDARY

* multipart form data
```

### view file

```http
GET /<file> HTTP/1.1
Host: nice.website
```

### advanced usage suggestions

create a fancy upload gui, drop it into the database under `index`

## contributing

wait until hacktoberfest

## license

Licensed under ISC. See [LICENSE.md](LICENSE.md)
