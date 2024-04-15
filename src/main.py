import pandas as pd

# Define the path to the Excel file
excel_file = 'patient_data.xlsx'

# Load the Excel file into a DataFrame
df = pd.read_excel(excel_file)

# Iterate over the rows in the DataFrame
for index, row in df.iterrows():
    # Create a new EDI 834 transaction file for each patient
    with open(f'834_{index}.X12', 'w') as f:
        # Write the ISA segment
        f.write('ISA*00*          *00*          *ZZ*SENDERID       *ZZ*RECEIVERID     *030101*1253*U*00401*000000001*0*P*>~\n')
        
        # Write the GS segment
        f.write('GS*BE*SENDERCODE*RECEIVERCODE*19991231*0802*1*X*004010X095A1~\n')
        
        # Write the ST segment
        f.write('ST*834*0001~\n')
        
        # Write the BGN segment
        f.write('BGN*00*ReferenceIdentification*19991231*Time*TimeZoneCode**2~\n')
        
        # Write the REF segment
        f.write('REF*38*ApplicationReceiverCode~\n')
        
        # Write the N1 segment
        f.write('N1*P5*PlanSponsorName*FI*PlanSponsorTaxId~\n')
        
        # Write the INS segment
        f.write(f'INS*{row["RelationshipCode"]}*{row["MemberActionCode"]}**{row["MaintenanceTypeCode"]}**{row["MaintenanceReasonCode"]}**{row["BenefitStatusCode"]}**{row["MedicareStatusCode"]}**{row["COBRACode"]}**{row["EmploymentStatusCode"]}**{row["StudentStatusCode"]}**{row["HandicapIndicator"]}**{row["DateOfBirth"]}~\n')
        
        # Write the REF segment
        f.write(f'REF*0F*{row["MemberPolicyNumber"]}~\n')
        
        # Write the DTP segment
        f.write(f'DTP*336*D8*{row["CoverageStartDate"]}~\n')
        
        # Write the NM1 segment
        f.write(f'NM1*IL*1*{row["LastName"]}*{row["FirstName"]}**{row["MiddleName"]}**{row["NamePrefix"]}**{row["NameSuffix"]}~\n')
        
        # Write the N3 segment
        f.write(f'N3*{row["AddressLine1"]}*{row["AddressLine2"]}~\n')
        
        # Write the N4 segment
        f.write(f'N4*{row["City"]}*{row["State"]}*{row["PostalCode"]}*{row["CountryCode"]}~\n')
        
        # Write the DMG segment
        f.write(f'DMG*D8*{row["DateOfBirth"]}*{row["GenderCode"]}**{row["MaritalStatusCode"]}**{row["RaceOrEthnicityCode"]}**{row["CitizenshipStatusCode"]}**{row["CountryCode"]}~\n')
        
        # Write the HD segment
        f.write(f'HD**{row["InsuranceLineCode"]}**{row["PlanCoverageDescription"]}~\n')
        
        # Write the DTP segment
        f.write(f'DTP*348*D8*{row["CoverageStartDate"]}~\n')
        
        # Write the SE segment
        f.write('SE*22*0001~\n')
        
        # Write the GE segment
        f.write('GE*1*1~\n')
        
        # Write the IEA segment
        f.write('IEA*1*000000001~\n')

# Print a success message
print("EDI 834 transaction files were successfully generated for each patient.")

