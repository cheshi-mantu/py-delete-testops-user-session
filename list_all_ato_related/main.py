import os
import sys
import redis
import jwt
import time

def list_data(r):
    for key in r.scan_iter("allure:testops:*:*", 250):
        print(key)

def scan():
    r = redis.from_url(os.environ.get("REDIS_URL"))
    list_data(r)

if __name__ == '__main__':
    scan()
