Autorization in Layers

1. Token Service - what scopes are services are allowed to be requested?
2. API Gateway - coarse grained check of scopes, token validity etc | coarse grained access control decision based on the claims in the token
3. Backend API - fine grained autorization of data(records, fields etc)released by API. Check claims, issuer, audience etc. | fine grained access control decision based on the token and the current request

Entitlement Management System 
- Open Policy Agent - OPA Engine
- Central place for autorization policy audit
- Cleaner application code and easier to maintain

- Authorization via the Entitlement Management System - OPA
- Called from PEP (policy Enforcement Point) - API Gateway or backend API 

https://www.openpolicyagent.org/




# Validate token locally in API Gateway

Applications calls *Authorization Endpoint <code>/oauth2/authorise</code>* to request an authorization code

Applications calls *Token Endpoint <code>/oauth2/token</code>* to request an OAuth token

```mermaid
sequenceDiagram
    participant UA as User-Agent
    participant AR as Authorization Server(IDP)
    participant AG as API Gateway
    participant RS as Resource Server

    UA->>AR: 1. Request Authorization Code to Authorization Endpoint
    AR-->>UA: 2. Return Authorization Code
    UA->>AR: 3. Request Token using Authorization Code to Token Endpoint
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


| Grant Flow | Description | Use Case |
| --- | --- | --- |
| Authorization Code | It is the most used grant type to authorize the Client to access protected data from a Resource Server. | Used by the secure client to get access token on behalf of their end user from a web server or a 3rd Party Developer Apps. |
| Implicit | It is intended for user-based clients who can’t keep a client secret because all the application code and storage is easily accessible. | Used by the client that can’t protect a client secret/token, such as a mobile app or single page application. |
| Client Credentials | This grant type is non-interactive way for obtaining an application access token using the provided client id/secret keys, outside of the context of a user. | It is suitable for application-to-application(A2A) or Partner/B2B authentication, not on behalf of a user.|
| Resource Owner password Credentials | It uses the username and the password credentials of a Resource Owner (user) to authorize and access protected data from a Resource Server. | For logging in with a username and password (only for first-party apps) |

Reference
https://techcommunity.microsoft.com/t5/azure-paas-blog/protect-api-s-using-oauth-2-0-in-apim/ba-p/2309538

