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
   
2. **Remove Duplicates**
   - Removed exact duplicate records.

3. **Drop Unnecessary Columns**
   - Removed the `Not_Useful_Column`.

4. **Clean Names**
   - Removed numbers and special characters from `Last_Name`.
   - Stripped whitespace from `First_Name` and `Last_Name`.

5. **Clean and Format Phone Numbers**
   - Removed all non-alphanumeric characters.
   - Standardized format to `xxx-xxx-xxxx`.
   - Removed missing or placeholder phone numbers.

6. **Split Address**
   - Split `Address` field into `Street_Address`, `City`, and `Zip_Code`.
   - Removed the original `Address` field.
   - Reordered columns for clarity.

7. **Standardize Categorical Columns**
   - Converted `Yes/No` values in `Paying_Customer` and `Do_Not_Contact` to `Y/N`.

8. **Handle Missing Data**
   - Replaced "N/a", "NaN", and "None" with empty strings.
   - Dropped customers who do not wish to be contacted.

## Tools Used

- **Python**
- **Pandas**
- **Excel** (for initial data input)

## Output

The cleaned dataset is ready for further analysis or use in a CRM system. All names, phone numbers, and addresses are standardized, and only relevant customers are retained.

