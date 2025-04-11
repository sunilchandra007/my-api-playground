# API Styles

## REST (Representational State Transfer)
- **Pros**: Simple, easy to use, follows web standards, supports caching and statelessness.
- **Cons**: Limited support for complex queries, can be inconsistent without a clear contract.
- **Use Cases**: Ideal for simple and stable data models, widely used in web services like Twitter and YouTube.

## SOAP (Simple Object Access Protocol)
- **Pros**: Strict contract, supports complex queries and operations, handles errors well.
- **Cons**: Complex and verbose, not scalable, adds overhead to existing protocols.
- **Use Cases**: Suitable for scenarios requiring high security and reliability, such as financial services.

## GraphQL
- **Pros**: Allows clients to request specific data, reduces over-fetching and under-fetching.
- **Cons**: Can be complex to set up and manage, requires careful schema design.
- **Use Cases**: Great for applications with dynamic and complex data requirements.

## gRPC (Google Remote Procedure Call)
- **Pros**: High performance, supports multiple languages, uses HTTP/2 for efficient communication.
- **Cons**: Requires more setup, less human-readable compared to REST.
- **Use Cases**: Suitable for real-time communication and microservices architecture.

## WebSocket

It enables full duplex communication between a server and a client over a long-running TCP connection.

It eliminates the needs for polling as required in HTTP, avoids some of the overhead of HTTP by reusing the same TCP connection for multiple request/responses resulting in a more efficient utilization of resources.

- **Pros**: Enables real-time, bidirectional communication, low latency. 
- **Cons**: More complex to implement, not suitable for all use cases.
- **Use Cases**: Ideal for applications requiring more interactive and live/real-time updates or continuous streams of data, such as chats, dashboard, finance stock info update, GPS, online education, live streaming and online gaming apps. 

## Webhooks
- **Pros**: Simple to implement, allows event-driven communication.
- **Cons**: Limited control over the timing of data delivery, requires endpoint management.
- **Use Cases**: Useful for notifications and real-time updates.
