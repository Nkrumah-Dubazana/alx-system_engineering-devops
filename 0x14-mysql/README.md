# MySQL Configuration and Backup

This project focuses on setting up MySQL database servers in a primary-replica architecture and automating database backups using Bash scripting.

## Tasks Overview

1. **MySQL Configuration - Primary Server**
   - File: [4-mysql_configuration_primary](./4-mysql_configuration_primary)
   - Description: Configuration file (`my.conf`) for the primary MySQL server, establishing it as the primary database server for the `tyrell_corp` database.

2. **MySQL Configuration - Replica Server**
   - File: [4-mysql_configuration_replica](./4-mysql_configuration_replica)
   - Description: Configuration file (`my.conf`) for the replica MySQL server, configuring it as the replica database server for the `tyrell_corp` database.

3. **Database Backup Script**
   - File: [5-mysql_backup](./5-mysql_backup)
   - Description: Bash script to automate database backups by generating compressed `tar.gz` archives from MySQL dumps. It backs up all databases on the root MySQL server.
     - Usage: `./5-mysql_backup <MySQL root password>`

## Usage Instructions

1. **MySQL Configuration Files Setup**
   - Download the `my.conf` configuration files for both the primary and replica MySQL servers.
   - Configure the MySQL servers according to the provided configurations.

2. **Database Backup Script Execution**
   - Download the `5-mysql_backup` Bash script.
   - Execute the script with the root password of the MySQL server to generate database backups.
     ```
     ./5-mysql_backup <MySQL root password>
     ```

## Additional Notes

- Ensure proper permissions and access control are in place for executing scripts and accessing MySQL servers.
- Regularly monitor the database servers and backup processes to ensure data integrity and availability.

---

This README provides an overview of the tasks completed in the MySQL configuration and backup project, along with instructions on how to use the provided scripts and configurations. If you have any questions or require further assistance, feel free to reach out!
