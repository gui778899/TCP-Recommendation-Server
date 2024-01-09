# TCP Server Project

## Overview
This TCP Server project offers a unique solution for recommending walking guides from books based on client preferences and facilitating book purchases. It features a MySQL database integration to handle user data, book information, and walk details.

## Database Design
The system uses a MySQL database with three primary tables:

- `buy`: Manages book purchase details.
- `search`: Contains walking routes and associated book information.
- `users`: Stores user transaction data.

### Database Export
The database schema and initial data can be exported into a `.sql` file, allowing easy setup and replication of the database environment.

## Code Description
The project is divided into two main scripts:

- `server.py`: Manages server-side operations, including client connection handling, database interactions, and concurrency management.
- `client.py`: Handles client-side functionalities such as connecting to the server and sending/receiving data for book searches and purchases.

## Key Functionalities
- **Concurrent Client Management**: Utilizes threading to handle multiple client connections simultaneously.
- **Walk Searching**: Clients can search for walks based on specific criteria like area, distance, and difficulty level.
- **Book Purchasing**: Enables clients to purchase books, with the database updating stock levels accordingly.
- **Input Error Handling**: Robustly handles various input errors, including case sensitivity issues.
- **Discount Offers**: Provides a 10% discount on purchases exceeding 75£.
- **Purchase Limitation**: Restricts clients from buying more than 8 books of the same number in one order.
- **Order Tracking Across Sessions**: Prevents stockpiling of books by the same client across different orders.
- **Stock Shortage Management**: Places excess book orders on back order if the stock is insufficient.

## Libraries
This project uses the following Python libraries:
- `mysql-connector`
- `mysql-connector-python`
- `mysql-connector-python-rf`

## Conclusion
The TCP Server project is a comprehensive system for recommending walking guides from books and managing book sales. It is designed to handle multiple clients, process transactions effectively, and ensure a user-friendly experience.
