# test-api

### An all too brief 'getting started'

Dependencies:

* Docker Engine (https://docs.docker.com/engine/install/)
* Docker Compose (https://docs.docker.com/compose/install/)

E.g.

```
git clone https://github.com/antony-s/test-api.git
cd ./test-api
docker-compose up
curl -i http://localhost:5000/vulnerabilities/392
```
*N.B. Responses returned as JSON (default) or XML depending on the request Accept header*

### Example usage with live demo

OpenAPI doc: `/api-docs`

e.g. http://34.105.225.194/api-docs

List endpoints: `/`

e.g. http://34.105.225.194/

List an endpoint: `/<endpoint>`

e.g. http://34.105.225.194/vulnerabilities

Display an endpoint item: `/<endpoint>/<sid>`

e.g. http://34.105.225.194/vulnerabilities/392

Filter examples:

* Vulnerabilities by asset: http://34.105.225.194/vulnerabilities?where={"affected_assets":35}
* Vulnerabilities by severity: http://34.105.225.194/vulnerabilities?where={"severity":"high"}
* Scans by scanner used: http://34.105.225.194/scans?where={"scanners":"Typhon"}
* Scans with two or more high severity counts: http://34.105.225.194/scans?where={"severity_counts.high":{"$gte":2}}

Misc:

Limit returned results and pagination: http://34.105.225.194/vulnerabilities?max_results=2&page=6
