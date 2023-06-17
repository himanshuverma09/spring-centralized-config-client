A Python client to fetch configuration from [Spring Config Server](https://spring.io/projects/spring-cloud-config).

This package relies on [requests](https://pypi.org/project/requests/).

## Installation

```shell
-> pip install spring-centralized-config-client
```

## General Usage

The very basic usage of this library looks like this:

```python
from spring_centralized_config_client.client import SpringCentralizedConfigClient

client = SpringCentralizedConfigClient(
          app_name="app-name", # Required App Name
          profile="dev", # Optional, Default=dev
          branch="main", # Optional, Default=main
          url="http://localhost:9000", # Optional, Default=http://localhost:9000
          auth_required=True, # Optional, Used to send if Authentication is required or not, Default=False
          username="username", # Required, If Auth Required is True, Default=Empty String
          password="password", # Required, If Auth Required is True, Default=Empty String
          flat_json=True, # Optional, If you want nested Json to be flatted, Default = False
          decrypt=True, # Optional, If you want to decrypt encryped configuration, Default = False
        )

print(client.get_config())
```

## TODO

- [x] Add support for Flat Json
- [x] Add support for Decryption 
- [ ] Add support for CloudFoundry

