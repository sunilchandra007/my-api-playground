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
