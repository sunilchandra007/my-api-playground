## JSON Web Token

JWE - Encrypted token
JWS - Signed token

JWT as Access token
- Should not have sesitive data in token
- Meant for resource server
- Bearer tokens are like cash, no one asks if you are the owner of the token
- Which algorithm alg to use for Signing or encryption?
  - Should whitelist secure algo only such as asymmetric(EC256) or symmetric(HS256|RS256)
  - alg as none means resource server would not validate the signature, so it is not recommended
- When to validate the token? ALWAYS, validate the signature
- Who provides the token? Authorization Server
- Always validate issuer and audience claim in the token
- For Open ID Connect, the value of issuer must be HTTPS URL
- Check for presence of scope claim in access token - ID tokens don't have it
- Tokens should have short expiration values - minutes or hours
   - exp - expiration
   - nbf - not before
   - iat - issued at
 - 
