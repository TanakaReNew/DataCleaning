# Customer Data Cleaning Project

This project demonstrates data cleaning and preprocessing using **Pandas** in Python. The dataset contains customer contact information with fields such as Customer ID, Name, Phone Number, Address, and subscription details. The goal of the project is to produce a clean, standardized dataset ready for analysis.

## Dataset

The dataset contains the following fields:

- Customer_ID
- First_Name
- Last_Name
- Phone_Number
- Address
- Paying_Customer
- Do_Not_Contact
- Not_Useful_Column (removed during cleaning)

## Steps in Data Cleaning

1. **Load Data**
   - Imported Excel file into Pandas DataFrame.
     <img width="1167" height="431" alt="1" src="https://github.com/user-attachments/assets/ba92e46c-78dc-4784-8982-1128898f180e" />

   
2. **Remove Duplicates**
   - Removed exact duplicate records.
   <img width="1090" height="139" alt="2" src="https://github.com/user-attachments/assets/94deb82e-7ef0-4a3e-9d8a-2c05843a393a" />
   <img width="1110" height="128" alt="3" src="https://github.com/user-attachments/assets/49cdd54a-d3bf-419f-9b6d-8b84db91161c" />


3. **Drop Unnecessary Columns**
   - Removed the `Not_Useful_Column`.
     <img width="958" height="329" alt="5" src="https://github.com/user-attachments/assets/96dfc064-ea34-4ff0-82e3-d32c864c7842" />


4. **Clean Names**
   - Removed numbers and special characters from `Last_Name`.
   - Stripped whitespace from `First_Name` and `Last_Name`.
     <img width="934" height="500" alt="6" src="https://github.com/user-attachments/assets/94382594-be9f-461a-83ea-f0e496f3d9e6" />


5. **Clean and Format Phone Numbers**
   - Removed all non-alphanumeric characters.
   - Standardized format to `xxx-xxx-xxxx`.
   - Removed missing or placeholder phone numbers.
     <img width="947" height="554" alt="7" src="https://github.com/user-attachments/assets/1231b4f4-13bc-4dbd-b9d3-a00e2ece49c2" />
      <img width="949" height="553" alt="8" src="https://github.com/user-attachments/assets/c95e5a3a-b0ca-470e-8057-f16d24a8748e" />

6. **Split Address**
   - Split `Address` field into `Street_Address`, `City`, and `Zip_Code`.
   - Removed the original `Address` field.
   - Reordered columns for clarity.
     <img width="1001" height="518" alt="10" src="https://github.com/user-attachments/assets/1c189162-02b5-4859-96f7-f625c6f3a92e" />


7. **Standardize Categorical Columns**
   - Converted `Yes/No` values in `Paying_Customer` and `Do_Not_Contact` to `Y/N`.
     <img width="1020" height="557" alt="11" src="https://github.com/user-attachments/assets/79271d8d-de06-419f-b17e-e04cb8a51296" />


8. **Handle Missing Data**
   - Replaced "N/a", "NaN", and "None" with empty strings.
   - Dropped customers who do not wish to be contacted.
     <img width="1051" height="599" alt="14" src="https://github.com/user-attachments/assets/de3fb905-3378-4a84-a756-64c003f1e1f6" />


## Tools Used

- **Python**
- **Pandas**
- **Excel** (for initial data input)

## Output

The cleaned dataset is ready for further analysis or use in a CRM system. All names, phone numbers, and addresses are standardized, and only relevant customers are retained.

