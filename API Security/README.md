# Authentication vs Authorisation

Authorization Server (Identity Platform - IdP)

Claims
- `sub` (Subject)
- `iss` (Issuer)
- `aud` (Audience)
- `exp` (Expiration)
- `scope` (Permissions)




| **Aspect**             | **Authentication**                                                                 | **Authorization**                                                                 |
|------------------------|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Purpose**            | Verifies **who you are**                                                           | Determines **what you can do**                                                   |
| **Token Type**         | **ID Token** – contains identity information                                       | **Access Token** – grants access to resources                                    |
| **Scope (Group of Claims)** | Typically includes `openid`, profile, email, etc.                                 | Defines roles, permissions, and access levels                                    |
| **Policy Type**        | **Authentication Policy** – governs identity verification                         | **Authorization Policy** – governs access control                                |
| **Token Usage**        | Used by client to prove identity to the application                                | Used by application to access protected resources                                |
| **Typical Standards**  | OpenID Connect (OIDC), SAML                                                             | OAuth 2.0                                                                         |
