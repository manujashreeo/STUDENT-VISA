This Python program is a simple management system for student visa records. It allows for the creation, retrieval, updating, and deletion of student visa entries, as well as checking visa validity and processing times. The system uses mock databases to simulate storing student information and visa processing status.



### Overview

The Student Visa Management System is a Python application designed to manage student visa records. It provides a simple interface for creating, reading, updating, and deleting visa entries. The system also assists users in checking visa validity and monitoring visa processing times.

### Features

- **CRUD Operations**: Create, read, update, and delete student visa records.
- **Visa Assistance**: Check if a student's visa is valid or if it requires renewal.
- **Processing Time Monitoring**: Track the processing duration for visa applications.

### Requirements

- Python 3.x
- No external libraries required

### Usage

1. **Create a Visa Record**:
   ```python
   create_student_visa(student_id, name, country, visa_expiry_date)
