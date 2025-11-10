Project Overview

This project demonstrates a containerized FastAPI application integrated with PostgreSQL and pgAdmin using Docker Compose.
It focuses on performing SQL operations — create, insert, query, update, and delete — while showcasing how relational databases interact with APIs in a modern DevOps workflow.

Technologies Used

FastAPI — Web framework for building APIs

PostgreSQL — Relational database

pgAdmin — GUI tool for PostgreSQL management

Docker Compose — Multi-container orchestration

GitHub Actions — Continuous Integration (CI) pipeline

Clone the Repository
git clone https://github.com/nishitanadimpalli/calculator-SQL.git
cd calculator-SQL

Build and Start Docker Containers
docker-compose up --build
SQL Operations Executed in pgAdmin

Create Tables
Defined users and calculations tables with foreign key constraints.

Insert Records
Added users (alice, bob) and several calculations.

Query Data
Used SELECT and JOIN statements to retrieve combined data.

Update Record
Modified the result of the add operation.

Delete Record
Deleted one calculation using the DELETE command.

Each of these steps was verified through screenshots (included in docs/Screenshots/SQL_Screenshots_Report_Final.docx).