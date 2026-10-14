Sender Application:

```bash

# 1. Create private key
openssl genrsa -out client.key 2048

# 2. Create CSR
openssl req -new \
-key client.key \
-out client.csr \
-subj "/CN=postman-client"

# 3. Generate a self-signed certificate
openssl x509 \
  -req \
  -days 365 \
  -in client.csr \
  -signkey client.key \
  -out client.crt

#4. Now you have
client.key   <-- private key
client.crt   <-- certificate

#self-signed
Subject DN: CN=postman-client
Issuer DN: CN=postman-client

```
Alternate to #3 is to share CSR with CA for signing
