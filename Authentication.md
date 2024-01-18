

## Authorization Endpoint
Applications call this endpoint <code>/oauth2/authorise</code> to request an authorization code



## Token Endpoint
Applications call this endpoint <code>/oauth2/token</code> to request an OAuth token


# Validate token locally in API Gateway
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

    User-Agent ->> API_Gateway: Initiate Logout Request
    API_Gateway ->> Authorization_Server: Revoke Access Token
    Authorization_Server -->> API_Gateway: Access Token Revoked
    API_Gateway ->> Resource_Server: Revoke Session
    Resource_Server -->> API_Gateway: Session Revoked
    API_Gateway -->> User-Agent: Logout Successful
```

# Validate token locally in API Gateway
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
    API_Gateway ->> API_Gateway: Validate Token Locally
    API_Gateway ->> Resource_Server: Forward Request
    Resource_Server -->> API_Gateway: Return Data
    API_Gateway -->> User-Agent: Return Data
```

# Logout scenario - Applications call this endpoint <code>/oauth2/logout</code> to log out the current user and end the user session.
```mermaid
sequenceDiagram
    participant User-Agent
    participant Authorization_Server
    participant API_Gateway
    participant Resource_Server

    User-Agent ->> API_Gateway: Initiate Logout Request
    API_Gateway ->> Authorization_Server: Revoke Access Token
    Authorization_Server -->> API_Gateway: Access Token Revoked
    API_Gateway ->> Resource_Server: Revoke Session
    Resource_Server -->> API_Gateway: Session Revoked
    API_Gateway -->> User-Agent: Logout Successful
```
