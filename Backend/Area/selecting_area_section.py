import os
import Backend.Area.shape_instruction



def shape_filtering(shape_number):
    if(shape_number == 1):
        
        os.system('cls')
        print("\033[1m" + "\t\tCircle" + "\033[0m")
        """ Backend.Combine_Object_Area.instruction_of_shapes.circle_instruction() """
        Backend.Area.shape_instruction.circle_instruction()
        """ print("Circle") """
     
             
    elif(shape_number == 2):
        
        os.system('cls')
        print("\033[1m" + "\t\tRectangle" + "\033[0m")
        """ Backend.Combine_Object_Area.instruction_of_shapes.rectangle() """
        Backend.Area.shape_instruction.rectangle()
        """ print("Rectangle") """
        
              
    elif(shape_number == 3):
        
        os.system('cls')
        print("\033[1m" + "\t\tTriangle" + "\033[0m")
        """ Backend.Combine_Object_Area.instruction_of_shapes.instruction_triangle() """
        Backend.Area.shape_instruction.instruction_triangle()
        """ print("Triangle") """
         
        
    elif(shape_number == 4):
       
        os.system('cls') 
        print("\033[1m" + "\t\tSquare" + "\033[0m")
        """ Backend.Combine_Object_Area.instruction_of_shapes.instruction_square() """
        Backend.Area.shape_instruction.instruction_square()
        """ print("Square") """
       
        
    else:
        
        os.system('cls')
        print("\t\tInvalid Number")