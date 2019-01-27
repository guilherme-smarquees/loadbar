import sys,os

circleMotor = 0

startedByZero = 0


def loadBar(count,total,countState=0,length=60,suffix='',typeBar=0):

    global startedByZero

    if(count == 0):
        startedByZero = 1

    if(startedByZero == 1):
        count += 1

    barLength = length
    filledLength = int(round(barLength * count /float(total)))
    percent = round(100.00 * count /float(total),1)
    
    if(typeBar == 0):
        bar = '=' * filledLength + '-' * (barLength - filledLength)
    elif(typeBar == 1):
        bar = '#' * filledLength + ' ' * (barLength - filledLength)
    elif(typeBar == 2):  
        if(count % 2 == 0):
            bar = ' ' * (filledLength - 1) + 'C'  + 'o' * (barLength - filledLength)
        else:
            bar = ' ' * (filledLength - 1) + 'O'  + 'o' * (barLength - filledLength)
    elif(typeBar == 3):
        bar = ' ' * (filledLength - 1) + '<o>'  + ' ' * (barLength - filledLength)
    elif(typeBar == 4):
        bar = ' ' * (filledLength - 1) + '=--->'  + ' ' * (barLength - filledLength)
    else:
        raise Exception('Invalid value of typeBar')
    
    if(countState == 1):
        sys.stdout.write('[%s]%s/%s %s%s ...%s\n'%(bar,count,total,percent,'%',suffix))
    elif(countState == 0):
        sys.stdout.write('[%s] %s%s ...%s\n'%(bar,percent,'%',suffix))
    else:
        raise IOError('INVALID VALUE countState')
    
    if(count != total):
        sys.stdout.write("\033[F")
    
    sys.stdout.flush()


def loadCircle(count,total,suffix=''):

    global circleMotor, startedByZero

    if(count == 0):
        startedByZero = 1

    if(startedByZero == 1):
        count += 1

    if(circleMotor == 0):
        sys.stdout.write('- [%s/%s] \n'%(count,total))
        
        if(count != total):
            sys.stdout.write('\033[F')
        
        sys.stdout.flush()
        circleMotor += 1
    elif(circleMotor == 1):
        sys.stdout.write('\ [%s/%s] \n'%(count,total))
        
        if(count != total):
            sys.stdout.write('\033[F')
        
        sys.stdout.flush()
        circleMotor += 1
    elif(circleMotor == 2):
        sys.stdout.write('| [%s/%s] \n'%(count,total))
        
        if(count != total):
            sys.stdout.write('\033[F')
        
        sys.stdout.flush()
        
        circleMotor += 1
    else:
        sys.stdout.write('/ [%s/%s] \n'%(count,total))
        
        if(count != total):
            sys.stdout.write('\033[F')
        
        sys.stdout.flush()
        circleMotor = 0
