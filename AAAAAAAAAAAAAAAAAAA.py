
'''
filename : SBappV4.py

Simple Billing System
Created on Dec 10, 2022
@author:MOK HO LUN
'''
import fileinput
import sys

data = []
clientDataList = []


def Checker(datafile): 
    test1 = open(datafile, 'r')
    lines = test1.read().split('\n')  
    for line in lines:
        if '_D_' not in line and '_C_' not in line:
            sys.stderr.write('\nInvalid transaction code:\n')
            wrongtrans = line
            sys.stderr.write(wrongtrans)
        else:
            if '-' in line:
                sys.stderr.write('\nInvalid transaction amt:\n')
                badamt = line
                sys.stderr.write(badamt)
        test1.close()
        
def displayFile(datafile):
    for line in fileinput.input(datafile):
        sys.stdout.write(line)
        
def readAndupdateClientDataList(datafile):
    fileIn = open(datafile, 'r')

    lines = fileIn.read().splitlines()
    for line in lines:
        transactionRecord = line.split('_')
        data.append(transactionRecord)
        
    for e in data:
        i = 0
        while i < len(clientDataList) and clientDataList[i]['Name'] != e[0]:
            i  += 1

        if i == len(clientDataList):
            if e[2] == 'C':
                clientDataList.append(dict(zip(['Name','Address','Balance'],
                                                       [e[0], e[1], -float(e[3])])))
            else:
                clientDataList.append(dict(zip(['Name','Address','Balance'],
                                                       [e[0], e[1], float(e[3])])))
        else:
            if e[2] == 'C':
                clientDataList[i]['Balance'] -= float(e[3])
            else:
                clientDataList[i]['Balance'] += float(e[3])
                
    fileIn.close()
    
def menuItem2():
        
    print('%-20s%-30s%5s%10s'%('Name','Address','Txn', 'Ampunt'))
    print('='*65)
    for e in data:
        print('%-20s%-30s%5s%10s'%(e[0], e[1], e[2], e[3]))
     
def main():
    instructions = """\nEnter one of the following:
        1 to print the contents of input transaction file
        2 to print all valid input transaction data
        3 to enter adjustment transaction
        4 to print customer report
        Q to end \n"""
    
       
    while True:
        sys.stdout.write(instructions) 
        sys.stdout.flush()      
        choice = input( "Enter 1 to 4 " ) 
        if choice == "1":
            displayFile(sys.argv[1])
        elif choice == "2":
            menuItem2()
        elif choice == "3":
            customerName = input('Enter Customer name: ')
            transactionType = input('Enter Transaction type (C/D): ')
            transactionAmt = input('Enter transaction amount : ')
            
            i = 0
            while i < len(clientDataList) and clientDataList[i]['Name'] != customerName:
                i  += 1

            if transactionType == 'C':
                clientDataList[i]['Balance'] -= float(transactionAmt)
            else:
                clientDataList[i]['Balance'] += float(transactionAmt)
                
            print('%-20s%-30s%10s'%('Name','Address','Balance'))
            print('='*60)
            for e in sorted(clientDataList, key = lambda c: c['Name']):
                if e['Balance'] != 0:
                    print('%-20s%-30s%10.2f'%(e['Name'], e['Address'], e['Balance']))   
            
        elif choice == "4":

            print('%-20s%-30s%10s'%('Name','Address','Balance'))
            print('='*60)
            for e in sorted(clientDataList, key = lambda c: c['Name']):
                if e['Balance'] != 0:
                    print('%-20s%-30s%10.2f'%(e['Name'], e['Address'], e['Balance']))
            
        elif choice == "Q":
            break
    print ("End Simple Billing System")
    
if __name__ == "__main__":
    sys.argv = [sys.argv[0], 'datafile1.dat']
    displayFile(sys.argv[1])
    readAndupdateClientDataList(sys.argv[1])
    main()



