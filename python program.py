import datetime

# Mock database to store student visa records
student_visa_db = {}
visa_processing_db = {}

class StudentVisa:
    def __init__(self, student_id, name, country, visa_expiry_date):
        self.student_id = student_id
        self.name = name
        self.country = country
        self.visa_expiry_date = visa_expiry_date
        self.status = "Valid"

# CRUD Operations for Student Visa Records
def create_student_visa(student_id, name, country, visa_expiry_date):
    if student_id in student_visa_db:
        return f"Student ID {student_id} already exists!"
    
    student_visa_db[student_id] = StudentVisa(student_id, name, country, visa_expiry_date)
    return f"Visa record created for student {student_id}"

def read_student_visa(student_id):
    student_visa = student_visa_db.get(student_id)
    if not student_visa:
        return f"No visa record found for student {student_id}"
    
    return vars(student_visa)

def update_student_visa(student_id, name=None, country=None, visa_expiry_date=None):
    student_visa = student_visa_db.get(student_id)
    if not student_visa:
        return f"No visa record found for student {student_id}"
    
    if name:
        student_visa.name = name
    if country:
        student_visa.country = country
    if visa_expiry_date:
        student_visa.visa_expiry_date = visa_expiry_date
    
    return f"Visa record updated for student {student_id}"

def delete_student_visa(student_id):
    if student_id not in student_visa_db:
        return f"No visa record found for student {student_id}"
    
    del student_visa_db[student_id]
    return f"Visa record deleted for student {student_id}"

# Assist with obtaining or renewing student visas
def assist_with_student_visa(student_id):
    student_visa = student_visa_db.get(student_id)
    
    if not student_visa:
        return f"No visa record found for student {student_id}"
    
    # If the visa is expired, mark it for renewal
    today = datetime.date.today()
    if today >= student_visa.visa_expiry_date:
        student_visa.status = "Renewal Required"
        return f"Visa for student {student_id} has expired. Renewal assistance required."
    else:
        return f"Visa for student {student_id} is valid until {student_visa.visa_expiry_date}. No renewal required."

# Monitor visa processing times (mock functionality)
def monitor_visa_processing_times(processing_id):
    processing_time = visa_processing_db.get(processing_id)
    
    if not processing_time:
        return f"No processing information found for ID {processing_id}"
    
    elapsed_time = datetime.date.today() - processing_time['start_date']
    
    return f"Processing time for {processing_id} is {elapsed_time.days} days."

# Add processing information (for testing purposes)
def add_visa_processing_time(processing_id, start_date):
    visa_processing_db[processing_id] = {
        'start_date': start_date
    }
    return f"Visa processing started for ID {processing_id} on {start_date}"

# Sample data
create_student_visa(1, "John Doe", "USA", datetime.date(2025, 5, 15))
create_student_visa(2, "Jane Smith", "Canada", datetime.date(2023, 9, 10))
add_visa_processing_time(1001, datetime.date(2023, 8, 1))

# Example usages
print(read_student_visa(1))
print(assist_with_student_visa(2))
print(monitor_visa_processing_times(1001))

