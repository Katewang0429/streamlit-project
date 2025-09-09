import hashlib, json

def hash_config(*args, **kwargs):
    payload = {"args": args, "kwargs": kwargs}
    s = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    return hashlib.md5(s).hexdigest()
