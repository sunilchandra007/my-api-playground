- [RFC 9700 - Best Current Practice for OAuth 2.0 Security](https://www.rfc-editor.org/rfc/rfc9700)
- [OAuth 2.1: What’s new, what’s gone, and how to migrate securely](https://workos.com/blog/oauth-2-1-whats-new)

---

## 👤 Authorization Code Flow with PKCE (for user-facing apps)

This is the **recommended flow for SPAs and mobile apps** and now even for confidential clients such as web apps in OAuth 2.1 draft.
> Front Channel(Browser doing HTTP request) + Back Channel(Backend Server doing HTTP calls)
### 🔄 How It Works:
1. App redirects user to the authorization server with:
   - `response_type=code`
   - A **code challenge** (from PKCE)
2. User logs in and consents.
3. Authorisation Server redirects back to Redirect URI/ Callback with an **authorization code**.
4. App sends the code + **code verifier** (dynamically generated secret) to the token endpoint.
5. Server verifies the code challenge and returns an **access token** (and optionally a refresh token).

### ✅ Benefits:
- Keeps tokens out of the browser URL.
- Prevents interception attacks.
- Supports refresh tokens.
- Secure for public clients (no client secret needed).

### Reference:
- [RFC 6749 – OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749)
- [📄 RFC 7636 – Proof Key for Code Exchange (PKCE)](https://www.rfc-editor.org/rfc/rfc7636)
- [OAuth Debugger Playground](https://oauthdebugger.com/)


---

## 🔌 Device Authorization Flow (for non-browser interfaces)

This flow is designed for **devices without browsers or keyboards**, such as smart TVs, IoT devices, or CLI tools.

### 🔄 How It Works:
1. Device requests authorization from the authorization server.
2. Server responds with:
   - A **user code**
   - A **verification URL**
   - A **device code**
3. Device displays:
   > “Go to https://example.com/device and enter code ABC123”
4. User opens the URL on another device, logs in, and enters the code.
5. Device **polls** the server with the device code.
6. Once authorized, the device receives an **access token**.

### ✅ Benefits:
- Works on devices without browsers.
- Keeps credentials off the device.
- Secure and user-friendly.

### 📄 Defined in:
- [RFC 8628 – OAuth 2.0 Device Authorization Grant](https://www.rfc-editor.org/rfc/rfc8628)

---


