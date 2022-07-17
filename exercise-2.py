def transformStr(str):

    if(str[0].lower()=='l'):
        str = str.lower()
    elif (str[0].lower()=='u'):
        str = str.upper()

    if (len(str)>5):
        print(str[:5] + '...')
    else:
        print(str)

    

transformStr('Testing string') # 'Testi...' (довжина більше 5 символів)
transformStr('Lux') # 'lux' (Починается на L)
transformStr('up') # 'UP' (Починается на U)
transformStr('Luxery') # 'luxer...' (Починается на L + довжина більше 5 символів)




