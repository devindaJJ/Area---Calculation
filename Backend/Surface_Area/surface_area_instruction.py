import Backend.Area.obstacle_class as surface_method
import Backend.Surface_Area.surface_area_of_objects as obb

def circle():
    
    
    radius = 0
    print("* To calculate Surface area of a circle, You Have to input Radius of Circle")
    print("* Area = π * r^2")
    print("* r = Radius (m)\n")
    
    try:
        
        radius_of_circle = float(input("Enter The Radius Of Circle : "))
        surface_circle = surface_method.Circle(radius_of_circle)
        surface_area = surface_circle.surface_area()
        print("-------------------------------------")
        print("The Area Of The Circle is ",surface_area,'m\u00b2')
        
    except:
        
        print("---- Please Enter The Decimal Number ----")
    
    

def cylinder():
    
    radius_of_circle = 0
    height_of_cycilder = 0
    print("* To calculate Surface area of a Cylinder, You Have to input Radius of Cylinder and Height")
    print("* Surface Area = 2πr^2 + 2πrh")
    print("* r = Radius (m)")
    print("* h = Height (m)")
    
    
    try:
        radius_of_cylinder = float(input("Enter The Radius Of Cylinder : "))
        height_of_cycilder = float(input("Enter The Heght Of Cylinder : "))
        surface_area_cylinder = obb.Cylinder(radius_of_cylinder, height_of_cycilder)
        area = surface_area_cylinder.surface_area()
        print("-------------------------------------")
        print("The Area Of The Circle is ",area,'m\u00b2')
    
    except:
        print("---- Pleace Enter The Decimal Number ----")
    
    

def rectangle():
    
    
    print("=---------------=")
    print("=               =")
    print("=               =")
    print("=               =")
    print("=---------------=\n")
    print("* To calculate Surface Area of a Rectangle, You Have to input Width , Height , Depth")
    print("* Surface Area = Rectangle ")
    print("* w = Width (m)")
    print("* h = Height (m)\n")
    
    
    try:
        
        width_of_rectangle = float(input("Enter The Width of Rectangle : "))
        height_of_rectangle = float(input("Enter The Heght Of Rectangle : "))
        rectangle_obj = surface_method.Rectangle(width_of_rectangle, height_of_rectangle)
        area_of_rectangle = rectangle_obj.surface_area()
        area_of_rectangle = round(area_of_rectangle,2)
        print("-------------------------------------")
        print("The Area Of The Rectanglr is ",area_of_rectangle,'m\u00b2')
    
    except:
        print("---- Please Enter The Decimal Number ----")
    
def instruction_cube():
    
    
    print("* To calculate surface area of a Cube, You Have to input width : ")
    print("* Surface Area = '(Width X Width) X 6'")
    print("* w = Width (m)\n")
    
    
    try:
        
        width_of_cube = float(input("Enter The Width of Cube : "))
        rectangle_obj = obb.Cube(width_of_cube)
        area_of_cube = rectangle_obj.surface_area()
        area_of_cube = round(area_of_cube,2)
        print("-------------------------------------")
        print("The Area Of The Rectanglr is ",area_of_cube,'m\u00b2')
    
    except:
        print("---- Please Enter The Decimal Number ----")
    
    

    


def sphere_object():
    
    print("* To calculate Surface area of a Sphere, You Have to input Radius.")
    print("* Surface Area = '4πr^2'")
    print("* r = Radius (m)\n")
    
    
    
    try:
        
        radius_sphere = float(input("Enter The Radius of Sphere : "))
        rectangle_obj = obb.Sphere(radius_sphere)
        area_of_rectangle = rectangle_obj.surface_area()
        area_of_rectangle = round(area_of_rectangle,2)
        print("-------------------------------------")
        print("The Area Of The Rectanglr is ",area_of_rectangle,'m\u00b2')
    
    except:
        print("---- Please Enter The Decimal Number ----")



def con_ins():
    
    print("* To Calculate Surface area of Cone, You Have to input Radius and slant height")
    print("* Surface Area = 'π*r^2*l'")
    print("* r = Radius (m)\n")
    print("* l = Slant Height (m)")
    
    try:
        
        radius_of_cone = float(input("Enter The Radius Of Cone : "))
        slant_height = float(input("Enter The Slant Height Of Cone : "))
        con_obj = obb.Cone(radius_of_cone, slant_height)
        area_of_cone = con_obj.surface_area()
        print("-------------------------------------")
        print("The Surface Area Of The Cone is ",area_of_cone,'m\u00b2')
        
    except:
        
        print("---- Pleace Enter Decimal Number ----")
        
        
        
def cuboid_instruction():
    
    
    print("* To Calculate Surface Area of Cuboid, You Have to input Width , Height and Length")
    print("* Surface Area = 2(Length * Width + Length * Height + Width * Heigth)")
    print("* W = Width (m)")
    print("* L = Length (m)")
    print("* H = Heigth (m)")
    
    try:
        
        width_of_cuboid = float(input("Enter The Width Of The Cuboid : "))
        height_of_cuboid = float(input("Enter The Height Of The Cuboid : "))
        length_of_cuboid = float(input("Enter The Length Of The Cuboid : "))
        
        cub_obj = obb.Cuboid(width_of_cuboid, height_of_cuboid, length_of_cuboid)
        area_of_cuboid = cub_obj.surface_area()
        
        
        print("--------------------------------------")
        print("The Surface Area Of The Cuboid is ",area_of_cuboid,'m\u00b2')
        
    
    except:
        
        print("---- Please Enter The Decimal Number ----")
    