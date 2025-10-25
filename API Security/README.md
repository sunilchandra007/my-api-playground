# Authentication vs Authorisation

Authorization Server (Identity Platform)

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
| **Validation Target**  | Identity of the user                                                               | Permissions and access rights                                                    |
| **Token Usage**        | Used by client to prove identity to the application                                | Used by application to access protected resources                                |
| **Management System**  | **Identity Provider (IdP)** – e.g., Azure AD, Auth0                                | **Entitlement Management System** – e.g., Azure AD roles, IAM policies           |
| **Typical Standards**  | OpenID Connect (OIDC), SAML                                                             | OAuth 2.0                                                                         |
