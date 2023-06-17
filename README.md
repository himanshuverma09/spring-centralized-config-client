A Python client to fetch configuration from [Spring Config Server](https://spring.io/projects/spring-cloud-config).

This package relies on [requests](https://pypi.org/project/requests/) library.

## Installation

```shell
pip install spring-centralized-config-client
```

## General Usage

```python
from spring_centralized_config_client.client import SpringCentralizedConfigClient

client = SpringCentralizedConfigClient(
          app_name="app-name", # Required App Name
          profile="dev", # Optional, Default=dev
          branch="main", # Optional, Default=main
          url="http://localhost:9000", # Optional, Default=http://localhost:9000
          auth_required=True, # Optional, Enable basic authentication, Default=False
          username="username", # Optional, Required if Auth Required is True, Default=Empty String
          password="password", # Optional, Required if Auth Required is True, Default=Empty String
          flat_json=True, # Optional, If you want nested Json to be flatted, Default = False
          decrypt=True, # Optional, If you want to decrypt encryped configuration, Default = False
        )

print(client.get_config())
```

## TODO

- [x] Add support for Flat Json
- [x] Add support for Decryption 
- [ ] Make decryption call in parallel

