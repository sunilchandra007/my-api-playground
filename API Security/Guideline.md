- [RFC 9700 - Best Current Practice for OAuth 2.0 Security](https://www.rfc-editor.org/rfc/rfc9700)
- [OAuth 2.1: What’s new, what’s gone, and how to migrate securely](https://workos.com/blog/oauth-2-1-whats-new)


OAuth 2.1 removes the **Implicit Grant** entirely.

📄 RFC 7636 – Proof Key for Code Exchange (PKCE)

PKCE was introduced to secure public clients (like SPAs and mobile apps) using the Authorization Code Flow.
It mitigates authorization code interception attacks by requiring a dynamically generated secret (code_verifier).
OAuth 2.1 Draft **mandates PKCE for all Authorization Code flows**, even for confidential clients.
