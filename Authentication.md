

## Authorization Endpoint
Applications call this endpoint to request an authorization code
<code>/oauth2/authorise</code>


## Token Endpoint
Applications call this endpoint to request an OAuth token
<code>/oauth2/token</code>


```mermaid
sequenceDiagram
    participant User-Agent
    participant Authorization_Server
    participant API_Gateway
    participant Resource_Server

    User-Agent ->> Authorization_Server: Initiate Authorization Request
    Authorization_Server -->> User-Agent: Redirect to Authorization Server
    User-Agent ->> Authorization_Server: Provide Authorization Code
    Authorization_Server -->> User-Agent: Return Access Token
    User-Agent ->> API_Gateway: Access Protected Resource
    API_Gateway ->> Authorization_Server: Validate Token
    API_Gateway -->> Resource_Server: Forward Request
    Resource_Server -->> API_Gateway: Return Data
    API_Gateway -->> User-Agent: Return Data
```
