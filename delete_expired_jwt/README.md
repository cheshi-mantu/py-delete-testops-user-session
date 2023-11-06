# Delete Allure Testops jwt tokens from Redis database

## Dependencies 

`pip3 install redis PyJWT`

## Env variable to be added

`export REDIS_URL=redis://default:<redis_password>@<ip_or_fqdn>:6379"`


## Usage

```shell
python3 main.py <username> [check|clean]
```
