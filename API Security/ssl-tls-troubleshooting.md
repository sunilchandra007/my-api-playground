```bash
# Inspect certificate details
# -v (verbose) and -k (ignore cert errors)
curl -vk https://example.com

# Extract certificate from the TLS handshake
openssl s_client -connect example.com:443 -showcerts </dev/null 2>/dev/null | \
openssl x509 -outform PEM > server-cert.pem
```
