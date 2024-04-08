# EXCEL - EDI 834 Converter
Python program that will take in an Excel file containing healthcare enrollment data and convert into a file that is 834 EDI format compliant

# TODOs
- [ ] Finish 834 EDI format definations
- [ ] Create sample excel data
- [ ] Create sample 834 EDI file
- [ ] Create a function that will take in an Excel file and convert it into a 834 EDI file
- [ ] Create a function that will output the converted 834 EDI file

# EDI Format
834 EDI file format is a special electronic data interchange format to be exchanged between organizations and government entities.

EDI consists of a set of segments, each of which is a collection of elements. Each segment is identified by a three-character code, and each element within the segment is separated by a delimiter.

Example: 
```
ISA*00* *00* *ZZ*EMEDNYMCR *ZZ*8-DIGIT PLAN 
ID*191120*2020*^*00501*193240001*0*T*:~
GS*BE*EMEDNYMCR*ETIN*20191120*202000*193240001*X*005010X220A1~
ST*834*193240001*005010X220A1~
BGN*00*1932400000000001XF1932400000000001*20191120*202001****2~
QTY*TO*1~
N1*P5*MEDICAID*FI*141797357~
N1*IN**94*8-DIGIT PLAN ID~
INS*Y*18*021*28*A***AC~
REF*0F*XX99991X~
REF*17*XX99991X~
REF*3H*9919999999~
REF*ABB*XX99991X~
DTP*356*D8*20190101~
NM1*IL*1*SUBSCRIBER 1 LAST NAME*SUBSCRIBER 1 FIRST NAME*MI***34*999999991~
PER*IP**TE*9999991111~
N3*121 AYE ST~
N4*ANYTOWN*NY*12901**CY*36019~
DMG*D8*20010101*M**C~
LUI*LE*ITA**5~
LUI*LE*ITA**6~
eMedNY MCE 834 Test Scenarios & Sample Files
16
LUI*LE*ITA**7~
NM1*QD*1*CASE NAME~
HD*021**HLT**IND~
DTP*348*D8*20190101~
LX*1~
NM1*Y2*2******SV*
8
-DIGIT PLAN ID*72~
COB*P*7AC0Y25NP81*1~
DTP*344*D8*20190901~
DTP*345*D8*20191231~
NM1*36*2*MEDICARE
-A~
LS*2700~
LX*1~
N1*75*FAM IND~
REF*17*I~
LX*2~
N1*75*COE CODE~
REF*17*30~
DTP*007*D8*20190901
```
Example Excel Data:
```
Subscriber ID	Member ID	Name	Date of Birth 
123456789	987654321	John Doe	01/01/1980
123456789	987654322	Jane Doe	02/02/1990
```

# EDI Loops-Segment-Element Definitions
These segments, loops, and elements provide a structured way to exchange patient enrollment information electronically using the 834 EDI standard.

### Segments
Segments represent the basic building blocks of an EDI transaction set. 

In the context of the 834 EDI standard, segments convey specific pieces of information about the enrollment process.

- `ISA` (Interchange Control Header): Provides control information for the interchange, - including sender and receiver IDs, and control numbers.
- `GS` (Functional Group Header): Indicates the beginning of a functional group of related transactions.
- `ST` (Transaction Set Header): Identifies the start of an individual transaction set, in this case, an enrollment transaction.
- `BGN` (Beginning Segment): Contains information about the beginning of the transaction set, such as transaction type code and reference numbers.
- `REF` (Reference Identification): Provides reference information related to the transaction.
- `DTP` (Date/Time Reference): Conveys date or time information related to the transaction.
- `N1` (Name): Contains party name information, such as the name of the employer, payer, or subscriber.
- `INS` (Subscriber Information): Provides information about the subscriber, including identification and demographic details.
- `DMG` (Demographic Information): Contains demographic details about the subscriber, such as birth date and gender.
- `HD` (Health Coverage): Specifies the type of health coverage being enrolled in.
- `LX` (Transaction Set Line Number): Identifies individual occurrences of a loop within the transaction set.

### Loops
Loops are structures within the EDI standard that allow for repeating sets of segments. In the 834 EDI standard, loops are used to group related information together.

- Header Loop (`Loop 2000`): Contains information related to the overall enrollment transaction, such as subscriber information and effective dates.
- Detail Loop (`Loop 2100`): Contains detailed information about each individual enrolled member, including demographic data and coverage details.
- Trailer Loop (`Loop 2200`): Contains summary information or totals related to the enrollment transaction.

### Elements
Elements are the individual data fields within segments. In the context of the 834 EDI standard, elements convey specific pieces of information about the enrollment process. 

- **Subscriber ID**: Unique identifier for the subscriber.
- **Member ID**: Unique identifier for each enrolled member.
- **Name**: Subscriber or member's name.
- **Date of Birth**: Subscriber or member's date of birth.
- **Gender Subscriber**: or member's gender.
- **Effective Date**: Date when coverage becomes effective.
- **Termination Date**: Date when coverage ends.

# Usage
To clone and run this repository locally, follow these steps:

```bash
# Clone this repository
$ git clone https://github.com/AlphonseBrandon/excel-edi.git

# Change into the project directory
$ cd excel-edi

# Create and activate a virtual environment
$ python -m venv venv
$ source venv/bin/activate

# Install the required dependencies
$ pip install -r requirements.txt

```