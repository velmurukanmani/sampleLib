import hamming

option = int(input(
    'Press 1 for generating hamming code  \nPress 2 for finding error in hamming code\n\t Enter your choice:--\n'))

if (option == 1):  # GENERATE HAMMING CODE
    print('Enter the data bits')
    dataBits = input()
    hamming.HammingCode.generateHammingCode(dataBits)

elif (option == 2):  # DETECT ERROR IN RECEIVED HAMMING CODE
    print('Enter the hamming code received')
    hammingCode = input()
    hamming.HammingCode.detectErrorByHammingCode(hammingCode)

else:
    print('Option entered does not exist')
