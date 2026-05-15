# Authentication

> **Who are you? Show me your identity. Prove it.**

Authentication is the process of verifying the identity of a user or system.  
It ensures that the entity requesting access is who they **claim** to be.

>> 👤 User‑facing (interactive)
- 👉 Require human interaction and establish user identity

>> 🤖 System‑to‑system (non‑interactive)
- 👉 Authenticate applications / workloads, not people
---

## 🔹 Layer 1: Authentication (Who are you?) 
**How does the user prove who they are?**

> Proving identity using credentials

✅ Authentication methods
> 👤 User‑facing (interactive)
- Password  
- Passkey (WebAuthn / FIDO2)  
- One‑Time Password (OTP)  
- Biometrics (fingerprint, face, iris)  
- Smart card  
> 🤖 System‑to‑system (non‑interactive)
- Basic Authentication
- mTLS (Client Authentication) - Strong M2M authentication
👉 *This layer performs **credential verification***.

---

## 🔹 Layer 2: Identity Assertion / Federation  
**How is the authentication result communicated to an application?**
> Communicating identity across trust boundaries

✅ Authentication protocols
> 👤 User‑facing (interactive)
- OpenID Connect (OIDC) - Wraps user authentication
- SAML 2.0  - Browser‑based SSO

👉 *This layer performs **identity assertion***.

## 🔹 Layer 3: Authorization & Token Mechanics (What can you do?)  
**How is the authentication result communicated to an application?**
> Governing access after identity is established


❌ NOT authentication
✅ OAuth / token‑level mechanisms

- OAuth scopes / audiences
- Private‑Key JWT → client authenticates to Authorization Server
- DPoP → binds access token to client key
- mTLS token binding (OAuth mTLS) → different from mTLS auth

✅ Key property:

- Operates on tokens
- Assumes authentication already happened
- Concerns authorization and token abuse prevention
---
## 🔹 Additional Authentication & Security Mechanisms

### ✅ Basic Authentication
- **Category:** Authentication method  
- **Description:** Username and password sent with each request  
- **Purpose:** Proves knowledge of a secret  
- **Notes:** Simple, non‑federated, discouraged for modern APIs

---

### ✅ Mutual TLS (mTLS / Client Authentication)
- **Category:** Authentication method  
- **Description:** Client proves possession of a private key using a TLS certificate  
- **Purpose:** Strong cryptographic authentication (commonly M2M)  
- **Notes:** Identity derived from client certificate

---
## 🔹 Additional Authentication Mechanisms

### ✅ Basic Authentication
- **Intended usage:** ⚠️ User‑facing (legacy) | ✅ System‑to‑system (limited)
- **Category:** Authentication method  
- **Layer:** Layer 1 – Credential verification  

**What it is:**  
Username and password sent on every request (Base64 encoded).

**Why:**  
The client proves knowledge of a shared secret directly to the server.

**Notes:**
- No federation
- No identity assertion
- Credentials are replayed on every request
- Weak by modern standards; discouraged for new designs

---

### ✅ Mutual TLS (Client Authentication / mTLS)
- **Intended usage:** ❌ User‑facing | ✅ System‑to‑system
- **Category:** Authentication method  
- **Layer:** Layer 1 – Credential verification  

**What it is:**  
The client proves possession of a private key using a client certificate during the TLS handshake.

**Why:**  
Cryptographic proof of possession = strong authentication.

**Notes:**
- Common for machine‑to‑machine communication
- Client identity is derived from certificate subject / SAN
- No SAML or OIDC required
- Authentication occurs at transport layer (TLS)

---
---

### ⚠️ Demonstrating Proof of Possession (DPoP)
- **Category:** Token security mechanism (OAuth extension)  
- **Description:** Binds an access token to a client‑held cryptographic key  
- **Purpose:** Prevents token replay and theft  
- **Important:**  
  👉 DPoP is **not authentication**  
  👉 It augments OAuth **after authentication has already occurred**
---
## Types of Authentication

### 1. **[Basic Authentication](https://www.rfc-editor.org/rfc/rfc7617.html)**

[Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Authentication) is a simple authentication scheme built into the HTTP protocol. It involves sending a username and password with each request.

- **How it works:**
  - The client sends HTTP requests with an `Authorization` header containing a base64-encoded string of the format `username:password`.
  - The server decodes the string and verifies the credentials.

- **Pros:**
  - Easy to implement.
  - Supported by most HTTP clients and servers.

- **Cons:**
  - Credentials are sent with every request, making it vulnerable if not used over HTTPS.
  - No session management; credentials must be stored and sent repeatedly.
  - Not suitable for modern applications requiring more secure and flexible authentication.

- **Example:**
  ```http
  GET /protected/resource HTTP/1.1
  Host: example.com
  Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=

### 2. **[OpenID Connect (OIDC)](https://openid.net/developers/how-connect-works/) | Delegated Authorisation**

OpenID Connect is an identity layer built on top of the OAuth 2.0 protocol. It allows clients to verify the identity of users based on authentication performed by an authorization server.

- **How it works:**
  - The user is redirected to an Autorization Server (identity provider - IdP) for authentication.
  - Upon successful login, the IdP returns an **ID token** and optionally an access token.
  - The client uses the ID token to verify the user's identity.


- **Pros:**
  - Secure and modern authentication protocol.
  - Supports single sign-on (SSO).
  - Provides standardized identity information via ID tokens.
  - Widely adopted and supported by major identity providers (e.g., Google, Microsoft, Okta).


- **Cons:**
  - More complex to implement than basic authentication.
  - Requires proper handling of tokens and secure storage.


- **Example Flow:** 
  - User clicks "Login with Google/SingPass".
  - Redirected to Google/SingPass login page [OIDC Federation].
  - After successful login, redirected back with an **ID token**.
  - Application verifies the token and logs the user in.
 
- **Reference:**
  - [🔥 Video - OAuth 2.0 and OpenID Connect (in plain English)](https://www.youtube.com/watch?v=996OiexHze0)
  - [🔥 Video - Everything You Ever Wanted to Know About OAuth and OIDC](https://www.youtube.com/watch?v=8aCyojTIW6U)
  - [Singpass developer](https://docs.developer.singpass.gov.sg/docs)
  - [OIDC Debugger Playground](https://oidcdebugger.com/) | [OAuth Debugger Playground](https://oauthdebugger.com/)

### 3. **[Mutual TLS | Client Authentication](https://www.rfc-editor.org/rfc/rfc8705.html)**
### 4. **[Demonstrating Proof of Possession (DPoP)](https://www.rfc-editor.org/rfc/rfc9449.html)**
