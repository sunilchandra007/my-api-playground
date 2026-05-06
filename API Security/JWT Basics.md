## [JSON Web Token](https://www.rfc-editor.org/rfc/rfc7523.html)

> JWTs are not authentication — they are verifiable identity assertions issued by a trusted authority.

- JWS - Signed JWT ( header + payload + signature )
  - signed with private key => Asymmetric signed JWT (widely used)
  - signed with shared secret => Symmetric JWS
- JWE - Encrypted JWT ( 5 dots) - very limited


```
//decoded header
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "NMlOFrBDXaBtYLAYiNRmn"
}
```
**Signed JWT as Access token**
- Should not have sensitive data in token
- Meant for resource server
- Which algorithm alg to use for Signing?
  - Should whitelist secure algo only such as asymmetric(RS256|ES256)
  - Enterprise APIs SHOULD default to RS256.
- When to validate the token? ALWAYS, validate the signature
- Who issues the token? Authorization Server
- Always validate claims in the token
  - *iss* - Issuer - who issued and signed this token
  - *aud* - Audience - recipient(s) that the token is intended for
- For Open ID Connect, the value of issuer must be HTTPS URL
- Check for presence of *scope* claim in access token - ID tokens don't have it
- Tokens should have short lifetime with expiry usually less than  60 minutes
   - *exp* - expiry, *nbf* - not before, *iat* - issued at
  
## Bearer token
> Bearer tokens are like cash, no one asks if you are the owner of the token

## PoP (Proof of Possession)
adds an extra layer of security by requiring the client to prove it owns a cryptographic key associated with the token. Instead of just presenting the token (like a bearer token), the client signs requests with a private key.

## spiffe
https://spiffe.io/
