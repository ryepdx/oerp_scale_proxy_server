def json_headers(f):
    def wrapped(*args, **kwargs):
        resp = f(*args, **kwargs)
        resp.headers['Content-Type'] = 'application/json'
        return resp
    return wrapped

def max_age_headers(f):
    def wrapped(*args, **kwargs):
        resp = f(*args, **kwargs)
        resp.headers['Access-Control-Max-Age'] = 9999999
        return resp
    return wrapped

