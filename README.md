# excel-edi
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

# EDI Segment-Element Definitions
- `ISA`: Interchange Control Header
- `GS`: Functional Group Header
- `ST`: Transaction Set Header
- `BGN`: Beginning Segment
-` N1`: Name
- `INS`: Insured Benefit
- `REF`: Reference Identification
- `DTP`: Date or Time or Period
- `NM1`: Individual or Organizational Name
- `PER`: Administrative Communications Contact
- `N3`: Address Information
- `N4`: Geographic Location
- `DMG`: Demographic Information
- `LUI`: Language Use
- `HD`: Health Coverage
- `LX`: Transaction Set Line Number
- `COB`: Coordination of Benefits
- `LS`: Loop Header
- `LE`: Loop Trailer


