


def calculate_area(width:int, length:int):
    if width==length:
        return "This is a Square"
    
    return width*length


def main():
    length=int(input("enter the length "))
    width=int(input("enter the width "))
    
    area_of_reactangle=calculate_area(length, width)
    print(f"length = {length} width = {width} area of rectangle =", area_of_reactangle)
    
    


if __name__=="__main__":
    main()