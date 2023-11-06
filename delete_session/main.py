import os
import sys
import redis
import jwt
import time

def delete_session(name, r):
    for key in r.scan_iter("allure:testops:*", 250):
        print(key)
        if name in str(key):
            r.delete(key)

def scan(name):
    r = redis.from_url(os.environ.get("REDIS_URL"))
    scan_jwt(name, r)

if __name__ == '__main__':
    scan(sys.argv[1])
