import datetime

Biodata='Biodata'#for center aliegned text
Work_Exp='Work Experience'#for center aliegned text

#Gather information for BioData
f_name=input('Enter your First name: ')
print('Hello', f_name,end=', ')
l_name=input('Enter your Last name: ')

gender=input('''Enter 'M' for Male and 'F' for Female: ''')
if gender=='M' or gender=='m':
    gen='Male'
elif gender=='F' or gender=='f':
    gen='Female'

dob=input("Enter your Date of Birth (in DD/MM/YYYY): ")  
dob=datetime.datetime.strptime(dob,"%d/%m/%Y").date()

father_name=input('''Enter your Father's name: ''')
mother_name=input('''Enter your Mother's name: ''')

nationality=input('Enter your Nationality: ')

email=input('Enter your Email iD: ')
country_c=input('Enter the Country Code: ')
phn_no=int(input('Enter the Phone Number: '))
phn_no=str(phn_no) #making string

religion=input('Enter the name of your religion: ')

language=input('What are the language known by you?: ')

address=input('Enter your Current Address: ')

interest=input('Enter your interests: ')

experience=input('Enter your work experience (in not more than 300 words): ')

#Biodata Output
print(Biodata.center(50))

print('Name: ',end='                  '); print(f_name, l_name)

print('Mobile Number: ',end='                  ');print(country_c, phn_no)

print('Email: ',end='                  ');print(email)

print('Gender: ',end='                  ');print(gen)

print('Date of Birth: ',end='                  ');print(dob)

print('Nationality: ',end='                  ');print(nationality)

print('Religion: ',end='                  ');print(religion)

print('''Father's Name: ''',end='                  ');print('Mr. ',father_name)

print('''Mother's Name: ''',end='                  ');print('Mrs. ',mother_name)

print('Language known: ',end='                  ');print(language)

print('Interests/Hobbies: ',end='                  ');print(interest)

print('Address: ',end='                  ');print(address)

print()
print(Work_Exp.center(50))
print(experience)

