## [JSON Web Token](https://www.rfc-editor.org/rfc/rfc7523.html)

- JWS - Signed token ( header + payload + signature ) - Widely used
- JWE - Encrypted token ( 5 dots) - very limited

**JWT/JWS as Access token**
- Should not have sensitive data in token
- Meant for resource server
- Which algorithm alg to use for Signing or encryption?
  - Should whitelist secure algo only such as asymmetric(RS256|EC256) or symmetric(HS256)
- When to validate the token? ALWAYS, validate the signature
- Who provides the token? Authorization Server
- Always validate *issuer*, *audience* and *subject* claim in the token
- For Open ID Connect, the value of issuer must be HTTPS URL
- Check for presence of *scope* claim in access token - ID tokens don't have it
- Tokens should have short expiration values - usually =< 60 minutes
   - *exp* - expiration
   - *nbf* - not before
   - *iat* - issued at
  
## Bearer token
> Bearer tokens are like cash, no one asks if you are the owner of the token

## PoP (Proof of Possession)
Proof of Possession adds an extra layer of security by requiring the client to prove it owns a cryptographic key associated with the token. Instead of just presenting the token (like a bearer token), the client signs requests with a private key.

## spiffe
https://spiffe.io/
