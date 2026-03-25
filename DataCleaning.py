import pandas as pd

# reading an excel file and assigning it the variable df
df = pd.read_excel(r"C:\Users\tanak\Music\TANAKA\Customer Call List (1).xlsx")

# removing records that are exactly the same i.e CustomerID: 1020
df = df.drop_duplicates()

# removing unnecesary columns ie 'Not_Useful_Column' 
df = df.drop(columns = 'Not_Useful_Column')

# removing any numbers or special characters from the 'last_Name' field
df['Last_Name'] = df['Last_Name'].str.strip('1234567890-=/?,.<>":}{+_)(*&^%$#@!')

# removing any special characters from 'Phone_Number' field
df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','',regex = True)

# changed the 'Phone_Number' field from datatype into to str to be able to format it later
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))

# Formatted the 'Phone_Number' field so that it has the pattern xxx-xxx-xxxx where x is a digit
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

# Removing the not-available phone numbers
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--', '')
df['Phone_Number'] = df['Phone_Number'].str.replace('nan--', '')

# Breaking the 'Address' field into 3 by splitting where there are ','
df[['Street_Address', 'City', 'Zip_Code']] = df['Address'].str.split(',', n=2, expand = True)

# Removing the address field 
df = df.drop('Address', axis = 1)

# Reorganising
col = df.pop('Street_Address')
df.insert(4, 'Street_Address', col)
col1 = df.pop('City')
df.insert(5, 'City', col1)
col2 = df.pop('Zip_Code')
df.insert(6, 'Zip_Code', col2)

# Replacing 'No' with 'N' and 'Yes' with 'Y' in the 'Paying_Customer' and 'Do_Not_Contact' fields
df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y')

# Removing all the null data 
df = df.replace("N/a", '')
df = df.replace("NaN", '')
df = df.replace("None", '')

# Removing the null data
df = df.fillna('')

# Removing the contacts that dont want to be contacted
for x in df.index:
    if df.loc[x, 'Do_Not_Contact'] == 'Y':
        df.drop(x, inplace = True)
df





























