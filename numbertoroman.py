one='I'
five='V'
ten='X'
fifty='L'
hundred='C'
fivehundred='D'
thousand='M'
def convert_to_roman(num):
    string=str(num)
    if len(string)==1:
        if num<4:
            return(num*one)
        
        elif num>3 and num <9:
            diff=num-5
            if diff<0:
                return(abs(diff)*one+five)
            else:
                return(five+diff*one)
        if num==9:
            return one+ten
    elif len(string)==2:
        if num<40: 
            return(num//10*ten+convert_to_roman(num%10))
        elif num>39 and num<90:
            diff=num-50
            diff=diff//10
            if diff<0:
                return(abs(diff)*ten+fifty+convert_to_roman(num%10))  
            else:
                return(fifty+diff*ten+convert_to_roman(num%10)) 
        if num >= 90 and num<100:
            return ten+hundred+convert_to_roman(num%10)  
    elif len(string)==3:
        if num<400:
            return(num//100*hundred+convert_to_roman(num%100)) 
        elif num>399 and num<900:
            diff=num-500
            diff=diff//100
            if diff<0:
                return abs(diff)*hundred+fivehundred+convert_to_roman(num%100) 
            else:
                return fivehundred+diff*hundred+convert_to_roman(num%100)  
        if num>=900 and num<1000:
            return hundred+thousand+convert_to_roman(num%100)
    elif len(string)==4:
        if num<5000:
            return(num//1000*thousand+convert_to_roman(num%1000))    
       


for num in range(1,5000):    
    print(num," : ",convert_to_roman(num))