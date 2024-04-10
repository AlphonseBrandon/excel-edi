import pandas as pd
import pyx12

# Load Excel data (assuming you have an 'enrollment.xlsx' file)
excel_file = '../data/excel/enrollment.xlsx'
df = pd.read_excel(excel_file)

# Create an EDI 834 segment
def create_edi_segment(member_id, first_name, last_name, dob, gender, email, start_date, coverage_type):
    return f"NM1*IL*1*{last_name}*{first_name}***34*{member_id}~"

# Generate EDI content
edi_content = []
for _, row in df.iterrows():
    edi_segment = create_edi_segment(
        row['Member ID'], row['First Name'], row['Last Name'],
        row['Date of Birth'], row['Gender'], row['Email Address'],
        row['Plan Start Date'], row['Coverage Type']
    )
    edi_content.append(edi_segment)

# Create the EDI file
edi_file = '\n'.join(edi_content)
with open('../data/edi/enrollment_834.txt', 'w') as f:
    f.write(edi_file)

print("EDI 834 file created successfully!")

# You can now send 'enrollment_834.txt' to the relevant system.
