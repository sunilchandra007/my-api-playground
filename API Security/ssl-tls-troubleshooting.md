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

# Extract certificate from the TLS handshake
openssl s_client -connect example.com:443 -showcerts </dev/null 2>/dev/null | \
openssl x509 -outform PEM > my-server-cert.pem
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
