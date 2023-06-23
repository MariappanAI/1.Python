
class AllFunctions():    
    def Subfields():
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Subfields in AI are:")
        for temp in list:
            print(temp)
        return temp
    def OddEven():
        num=int(input("Enter the Number:"))
        if(num%2==0):
            print(num,"is Even Number")
            message="EVEN NUMBER"
        else:
            print(num,"is Odd Number")
            message="ODD NUMBER"
            return message
    def Eligible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Gender=="Male" and Age<=18):
            print("NOT EELIGIBLE")
        else:
            print("ELIGIBLE")
            return 
    def Percentage():
        Sub1=int(input("Subject1="))
        Sub2=int(input("Subject2="))
        Sub3=int(input("Subject3="))
        Sub4=int(input("Subject4="))
        Sub5=int(input("Subject5="))
        Total=Sub1+Sub2+Sub3+Sub4+Sub5
        print("Total:",Total)
        Percentage=Total/5    
        print("Percentage:",Percentage)
        return Total,Percentage
    def triangle():
        Height=float(input("Hieght:"))
        Breadth=float(input("Breadth:"))
        Area=Height*Breadth/2
        print("Area of Triangle:",Area)
        Height1=float(input("Hieght1:"))
        Height2=float(input("Hieght2:"))
        Breadth2=float(input("Breadth2:"))
        Perimeter=Height1+Height2+Breadth2
        print("Perimeter of Triangle",Perimeter)
        return Area,Perimeter