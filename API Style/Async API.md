https://blog.postman.com/understanding-asynchronous-apis/

Async APIs allow you to stream data, send multiple requests at the same time.
Async APIs tend to use bidirectional protocols like HTTP/2. 
The client and server can maintain their connection, sending and receiving data for as long as they need to.

Async APIs are essential for bidirectional streaming. The client and server can continuously send messages to one another. HTTP/2 supports this type of connection by default.

Use Case for Async APIs - Real time updates
Messaging | Social media | Mobile games | Banking | IOT

Examples of Async APIs
WebSockets | Server-Sent Events (SSE) | gRPC | Message Queuing Protocols (like RabbitMQ or Kafka)

Sync APIs require you to make a new request every time you need data.
Sync APIs often use HTTP, a unidirectional protocol. 
The client sends a request to the server, and then the server sends an HTTP response back.

While it is technically possible to stream data over HTTP (usually known as chunking), it adds complexity on the client side and you can be slowed down by buffer limits and other issues.

Use case for Sync APIs

To ensure that requests are processed in a specific order, synchronous API calls are a better fit. 
Synchronous APIs are also less complex to set up, so they’re still ideal for a straight forward request-response pattern.

Example of Sync APIs
REST | SOAP | GraphQL 

Not all API architectures fit neatly into the synchronous or asynchronous labels. For example, GraphQL can be considered synchronous because you send queries over HTTP, but it also supports asynchronous messaging using WebSockets with its subscription server. You can register with GraphQL subscription server to receive asynchronous updates, with the added benefit of choosing exactly which fields you want in the response.
