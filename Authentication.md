

## Authorization Endpoint
Applications call this endpoint <code>/oauth2/authorise</code> to request an authorization code

## Token Endpoint
Applications call this endpoint <code>/oauth2/token</code> to request an OAuth token



<details>

<summary>Local Token Validation</summary>

# Validate token locally in API Gateway
```mermaid
sequenceDiagram
    participant UA as User-Agent
    participant AR as Authorization Server(IDP)
    participant AG as API Gateway
    participant RS as Resource Server

    UA->>AR: 1. Initiate Authorization Request
    AR-->>UA: 2. Redirect to Authorization Server
    UA->>AR: 3. Request Token using Authorization Code
    AR-->>UA: 4. Return Access Token and Refresh Token

    UA->>AG: 5. Access Protected Resource with New Access Token
    AG->>AG: 6. Validate Access Token
    AG->>RS: 7. Forward Request
    RS-->>AG: 8. Return Data
    AG-->>UA: 9. Return Data


    UA->>AR: 10. Request Refresh Token
    UA->>AR: 11. Request New Access Token using Refresh Token
    AR-->>UA: 12. Return New Access Token
    AG->>AG: 13. Validate New Access Token
    AG->>RS: 14. Forward Request
    RS-->>AG: 15. Return Data
    AG-->>UA: 16. Return Data
```

</details>

# Logout scenario
Applications call this endpoint <code>/oauth2/logout</code> to log out the current user and end the user session.

```mermaid
sequenceDiagram
    participant UA as User-Agent
    participant AR as Authorization Server
    participant AG as API Gateway
    participant RS as Resource Server

    UA->>AG: 1. Initiate Logout Request
    AG->>AR: 2. Revoke Access Token
    AR-->>AG: 3. Access Token Revoked
    AG->>RS: 4. Revoke Session
    RS-->>AG: 5. Session Revoked
    AG-->>UA: 6. Logout Successful

```
