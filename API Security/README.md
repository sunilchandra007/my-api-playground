# Application type 

## Public applications
- cannot hold credentials securely.
- example
  - native desktop application, mobile application that uses *Authorization Code* Flow with *PKCE*
  - JavaScript-based client-side web application (such as a single-page app)

## Confidential applications 
- can hold credentials in a secure way without exposing them to unauthorized parties.
- require a trusted backend server to store the secret(s).
- example
  - web application with a secure backend that uses the *Authorization Code* Flow
  - machine-to-machine (M2M) application that uses the *Client Credentials* Flow ( client id + client secret)

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

## FAPI reference
- [A Comprehensive Commentary on Financial-grade API](https://storage.googleapis.com/authlete-website/resources/wp-commentary-on-fapi.pdf)
- https://openid.net/guest-blog-financial-grade-api-fapi-explained-by-an-implementer-updated/
- https://auth0.com/blog/fapi-2-0-the-future-of-api-security-for-high-stakes-customer-interactions/
- https://aiden.ziegelaar.io/the-developers-guide-to-financial-grade-apis-fapi

## API Security and Governance Standards
- [Singapore Gov - API Standards](https://docs.developer.tech.gov.sg/docs/api-governance-model)
- [Guidelines for API Protection](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-228-upd1.pdf)
- [OAuth 2.1 draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/)
