## Application Types

### Public Applications
Public applications **cannot securely store long‑term credentials (such as client secrets)** because the runtime environment is controlled by the end user or is otherwise untrusted.

As a result, **any embedded secret would be exposed**.

**Examples:**
- Native desktop applications
- Mobile applications using **Authorization Code Flow with PKCE**
- JavaScript‑based client‑side web applications (Single‑Page Applications)

**Characteristics:**
- No client secret
- Authenticates the *user*, not the application itself

---

### Confidential Applications
Confidential applications **can securely store credentials** without exposing them to unauthorized parties, because they run in a trusted environment (for example, a backend server).

They **require a trusted backend** to protect secrets or private keys.

**Examples:**
- Web applications with a secure backend using **Authorization Code Flow with PKCE**
- Machine‑to‑Machine (M2M) applications using
  - Client Credentials Flow (Client ID + client secret)
  - Private key JWT (strongly recommended for high‑security scenarios)
  - mTLS (advanced/regulated environments including B2B scenarios)

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
