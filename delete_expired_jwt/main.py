import os
import sys
import redis
import jwt
import time

def scan_jwt(name, r, mode):
    for key in r.scan_iter("allure:testops:jwt:*", 250):
        token = r.get(key)
        print(token)
        try:
            decoded = jwt.decode(token, options={"verify_signature": False})
            user = decoded["sub"]
            print("user:" + user)
            exp = decoded["exp"]
            print("expiration:" + exp)
        except:
            continue
        if user == name:
            print(key)
            if mode == "clean":
                r.delete(key)

def scan(name, mode):
    print(os.environ.get("REDIS_URL"))
    r = redis.from_url(os.environ.get("REDIS_URL"))
    scan_jwt(name, r, mode)

if __name__ == '__main__':
    scan(sys.argv[1], sys.argv[2] if sys.argv[2:] else "check")
