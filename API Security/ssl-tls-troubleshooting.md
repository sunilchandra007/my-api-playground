```
wget https://google.com
==========
Connecting to google.com (172.217.194.138:443)
tls_post_process_server_certificate:certificate verify 
ssl_client: SSL_connect
wget: error getting response: Connection reset by peer
==========
```

```bash
# Inspect certificate details
# -v (verbose) and -k (ignore cert errors)
curl -vk https://example.com

# Extract first certificate(from entire chain) from the TLS handshake
openssl s_client -connect example.com:443 -showcerts </dev/null 2>/dev/null | \
openssl x509 -outform PEM > my-server-cert.pem

# extract full chain
openssl s_client -connect example.com:443 -showcerts </dev/null 2>/dev/null > full-chain.pem

# split into seperate files (0-leaf> 1-intermediate > 2-root in the last)
openssl s_client -connect example.com:443 -showcerts </dev/null 2>/dev/null | \
awk '/BEGIN CERTIFICATE/{i++}{print > "cert" i ".pem"}'


# Print human readable details of the certificate
openssl x509 -in cert.pem -noout -text

# print Subject
openssl x509 -in cert.pem -noout -subject

# print Issuer
openssl x509 -in cert.pem -noout -issuer

# print fingerprint in SHA-256 format
openssl x509 -in cert.pem -noout -fingerprint -sha256

# check if hash(md5/sha256) of the modulus of cert and private key matches
openssl x509 -in cert.pem -noout -modulus | openssl md5
openssl x509 -in privkey.pem -noout -modulus | openssl md5


# Build ca-bundle.pem from intermediates only (skip leaf)
cat cert2.pem cert3.pem 2>/dev/null > ca-bundle.pem

# Validate the certificate chain (with a CA bundle)
openssl verify -CAfile ca-bundle.pem cert0.pem

```

## SSL issue
```bash
# download/copy container’s CA certificate bundle 
podman cp <container>:/etc/ssl/certs/ca-certificates.crt ./container-ca.crt
# use OpenSSL on the host to verify SSL connectivity using container's CA bundle
openssl s_client -connect example.com:443 -verify_return_error -CAfile ./container-ca.crt </dev/null
```

## SSl issue - fix
```bash
# export self-signed CA certificate and copy it to container
podman cp my-pg-root-ca.pem <container>:/usr/local/share/ca-certificates/my-ca.crt
# Update the trust store inside the container:
podman exec <container> update-ca-certificates
```
