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

