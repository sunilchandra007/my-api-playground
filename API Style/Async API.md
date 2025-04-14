# Understanding Asynchronous APIs

## **Asynchronous APIs**

### **Overview**
- **Operation**: Stream data, send multiple requests simultaneously.
- **Protocols**: Use bidirectional protocols like HTTP/2.
- **Advantages**: Faster communication, quicker response times, reliable scaling.

### **Use Cases**
- **Real-Time Updates**: Messaging, social media, mobile games, banking, IoT.

### **Examples**
- **WebSockets**
- **Server-Sent Events(SSE)**
- **gRPC**
- **Message Queuing Protocols**: MQTT, AMQP, RabbitMQ, Kafka

## **Synchronous APIs**

### **Overview**
- **Operation**: Client require a new request for each data retrieval from server as an HTTP response.
- **Protocols**: Often use HTTP, a unidirectional protocol.
- **Challenges**: Streaming data over HTTP(chunking) adds complexity to client side and can be slowed by buffer limits.

### **Use Cases**
- **Order Processing**: Ensuring requests are processed in a specific order.
- **Simplicity**: Ideal for straightforward request-response patterns.

### **Examples**
- **REST**
- **OData**
- **SOAP**
- **GraphQL**

## **Hybrid Approach**
- **GraphQL**: Can be synchronous (HTTP queries) and asynchronous (WebSockets for subscriptions).
- Not all API architectures fit neatly into the synchronous or asynchronous labels. For example, GraphQL can be considered synchronous because you send queries over HTTP, but it also supports asynchronous messaging using WebSockets with its subscription server. You can register with GraphQL subscription server to receive asynchronous updates, with the added benefit of choosing exactly which fields you want in the response.

### **References**
- [Understanding Asynchronous APIs](https://blog.postman.com/understanding-asynchronous-apis/)
- [API Management for Asynchronous](https://apidog.com/blog/api-management-for-asynchronous/)

