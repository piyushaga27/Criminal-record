#criminal data
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('criminal_data.csv',sep=',')
rew=list(df['reward'])
nme=list(df['name'])
city=list(df['city'])
city_dict={}
for i in city:
    city_dict[i]=city.count(i)
    


def allData():
    print('All Data is:')
    print('='*50)
    print(df)

def cityBasis():
    print('Detais on City basis')
    print('='*50)
    loc=input('ENTER CITY :')
    for b in city:
        if loc.upper()==b:
            print('Details are as follows . . . ')
            print(df[df['city']==loc.upper()])
            break
    else:
        print('City not Found')

def rewardBasis():
    print('='*50)
    print('Details on Reward Basis:')
    m='''1. REWARD GREATER THAN
2. REWARD LESSER THAN
3. REWARD EQUAL TOO
4. RETURN TO MAIN MENU'''
    print(m)
    c=input('ENTER YOUR CHOICE :')
    if c=='1':
        print('='*50)
        r=int(input('Enter Greater Than Reward Amount :'))
        print('='*50)
        print('Details are as follows :')
        print(df[df['reward']>=r])
    elif c=='2':
        print('='*50)
        r=int(input('Enter Lesser Than Reward Amount :'))
        print('='*50)
        print('Details are as follows :')
        print(df[df['reward']<=r])
    elif c=='3':
        print('='*50)
        r=int(input('Enter Reward Amount :'))
        print('='*50)
        print('Details are as follows :')
        print(df[df['reward']==r])
    elif c=='4':
        pass
    elif c=='':
        print('user input is required')
    else:
        print('Invalid Character')

def nameBasis():
    print('='*50)
    print('Details from Name . . .')
    print('='*50)
    nm=input('Enter Name of Criminal :')
    print('='*50)
    for x in nme:
        if nm.upper()==x:
            print(df[df['name']==nm.upper()])
            break
    else:
        print('Name not Found')
 
def menu():
    print('Criminal Data')
    print('''1. SHOW ALL DATA
2. INFORMATION ON CITY BASIS
3. IMFORMATION ON REWARD BASIS
4. DETAILS FROM NAME
5. CHARTS SECTION 
6. EXIT''')

def chartSection():
    print('='*50)
    print('CHARTS SECTION')
    mnu='''1. SHOW CHART ACCORDING TO CITY BASIS
2. SHOW CHART ACCORDING TO REWARD BASIS
3. MAIN MENU'''
    print(mnu)
    cho=input('ENTER YOUR CHOICE :')
    print('='*50)
    if cho=='1':
        
        print('CHART ON CITY BASIS')
        plt.bar(city_dict.keys(),city_dict.values(),color=['r','g','b','y'])
        plt.title('Criminal details on City basis')
        plt.ylabel('Number Of Criminal')
        plt.xlabel('City')
        print('Chart Displayed Sucessfully. . .')
        print('='*50)
        plt.show()
    elif cho=='2':
        
        print('CHART ON REWARD BASIS')
        plt.hist(rew,bins=10,color='g')
        plt.title('Criminal Details on Reward basis')
        plt.xlabel('Rewards')
        plt.ylabel('Number of Criminal')
        print('Histogram Displayed Sucessfully. . .')
        print('='*50)
        plt.show()

    elif cho=='3':
        pass
    
        
a=True
while a:
    print('='*50)
    menu()
    ch=(input('ENTER YOUR CHOICE :'))
    if ch=='1':
        allData()
    elif ch=='2':
        cityBasis()
    elif ch=='3':
        rewardBasis()
    elif ch=='4':
        nameBasis()
    elif ch=='5':
        chartSection()
    elif ch=='6':
        print('='*50)
        print('Thank You . . .')
        print('='*50)
        a=False
    elif ch=='':
        print('='*50)
        print('User Input is required:')
    else:
        print('='*50)
        print('Invalid Character')
        

