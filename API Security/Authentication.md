# Authentication

> **Who are you ? Show me your identity. Prove it!**

> Authentication is the process of verifying the identity of a user or system. It ensures that the entity requesting access is who they **claim** to be.


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
  - The user is redirected to an identity provider (IdP) for authentication.
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
  - Redirected to Google/SingPass login page.
  - After successful login, redirected back with an **ID token**.
  - Application verifies the token and logs the user in.
 
- **Reference:**
  - [🔥 Video - OAuth 2.0 and OpenID Connect (in plain English)](https://www.youtube.com/watch?v=996OiexHze0)
  - [Singpass developer](https://docs.developer.singpass.gov.sg/docs)
  - [OIDC Debugger Playground](https://oidcdebugger.com/)

### 3. **[Mutual TLS | Client Authentication](https://www.rfc-editor.org/rfc/rfc8705.html)**
### 4. **[Demonstrating Proof of Possession (DPoP)](https://www.rfc-editor.org/rfc/rfc9449.html)**
