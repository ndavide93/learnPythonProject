def read_int(prompt, min, max):
    v=prompt
    try:
        prompt=int(input("Enter a number from -10 to 10: "))
        if int(prompt) <= max and int(prompt) >= min:
            
            return v
        
        
    except ValueError:
        print('Error: wrong input')
        return False
    except float(prompt) >= max and (prompt) <= min:
        print('Error: the value is not within permitted range ' + str(min) + '.' + str(max))
        return False
    
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

 # try:
  #      prompt=(input("Enter a number from -10 to 10: ") )
 #       #v = prompt 
#        if float(prompt) <= max and (prompt) >= min: 
 #           return prompt
 #       else : 
 #           print('Error: the value is not within permitted range ' + str(min) + '.' + str(max))
#    except ValueError:
   #     print('Error: wrong input');
 #   
        
    # Write your code here.
    #
    