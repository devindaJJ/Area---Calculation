import Backend.Surface_Area.combined_suface_area


def selecting_surface_area(entered_value):
    
    if(entered_value == 1):
        
        print("Cube")
        Backend.Surface_Area.surface_area_instruction.instruction_cube()
        
    
    elif(entered_value == 2):
        print("Spher")
        Backend.Surface_Area.surface_area_instruction.sphere_object()
    
    elif(entered_value == 3):
        print("Cylinder")
        area = Backend.Surface_Area.combined_suface_area.cylinder()
        return area
        
    elif(entered_value == 4):
        print("Cone")
        area = Backend.Surface_Area.combined_suface_area.con_ins()
        return area
        
    elif(entered_value == 5):
        print("Cuboid")
        Backend.Surface_Area.surface_area_instruction.cuboid_instruction()
       
    
    else:
        print("--- Please Enter The Decimal Number ---")