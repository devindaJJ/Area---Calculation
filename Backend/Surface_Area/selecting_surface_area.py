import Backend.Surface_Area.surface_area_instruction


def selecting_surface_area(entered_value):
    
    if(entered_value == 1):
        
        print("Cube")
        Backend.Surface_Area.surface_area_instruction.instruction_cube()
        
    
    elif(entered_value == 2):
        print("Rectanle")
        Backend.Surface_Area.surface_area_instruction.sphere_object()
    
    elif(entered_value == 3):
        print("Cylinder")
        Backend.Surface_Area.surface_area_instruction.cylinder()
        
    elif(entered_value == 4):
        print("Cone")
        Backend.Surface_Area.surface_area_instruction.con_ins()
        
    elif(entered_value == 5):
        print("Cuboid")
        Backend.Surface_Area.surface_area_instruction.cuboid_instruction()
       
    
    else:
        print("--- Please Enter The Decimal Number ---")