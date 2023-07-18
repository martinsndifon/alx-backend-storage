## NoSQL
NoSQL, which stands for "Not Only SQL," is a database approach that diverges from the traditional relational database model. Unlike relational databases, which use structured tables with fixed schemas and SQL as the querying language, NoSQL databases offer a flexible and schema-less data model.

NoSQL databases are designed to handle large volumes of unstructured, semi-structured, and structured data. They are often used in scenarios where scalability, high availability, and performance are crucial. NoSQL databases provide horizontal scalability, allowing data to be distributed across multiple servers or clusters.

Here are some key characteristics and features of NoSQL databases:

Schema-less: NoSQL databases do not enforce rigid schemas, allowing for dynamic and flexible data structures. Data can be stored and retrieved without requiring a predefined schema.

Document-oriented: Many NoSQL databases use a document-oriented model, where data is stored in a self-describing document format, such as JSON or BSON. Each document can have its own structure and may contain nested data.

Key-Value Stores: Some NoSQL databases employ a simple key-value store model, where data is stored and retrieved using a unique key.

Columnar Databases: Column-oriented databases store data in columns rather than rows, making them well-suited for handling large datasets and analytical workloads.

Graph Databases: Graph databases are optimized for handling interconnected data and are ideal for scenarios involving complex relationships and graph-like structures.

High Scalability: NoSQL databases are designed for horizontal scalability, allowing them to handle massive amounts of data and high traffic loads by distributing data across multiple servers or clusters.

High Availability: NoSQL databases often provide built-in mechanisms for replication and fault tolerance, ensuring data availability even in the event of server failures.

Performance: NoSQL databases are optimized for read and write performance, enabling fast data access and data processing.

Flexibility: NoSQL databases can accommodate evolving data models and changing application requirements, making them suitable for agile development and rapid iterations.

NoSQL databases have gained popularity in modern applications, particularly in use cases such as web applications, big data analytics, real-time streaming, content management systems, and IoT applications. They offer an alternative approach to handling diverse and dynamic data requirements beyond the confines of traditional relational databases.

Modules like mongoengine can help achieve a structure like schema for working with a non relational database like MongoDB