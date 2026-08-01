# Task :
#                                  MENU :
#                                  [ 1 ] press 1 for add product name    
#                                  [ 2 ] press 2 for remove product name 
#                                  [ 3 ] press 3 for view prducts
#                                  [ 4 ] press 4 for show total product available
#                                  [ 5 ] remove all prodcut
#                          add :- do you want to perform more operation press y for yes and press n for no


flag = True
Product_list = []
while flag:
    print("\t\t\t MENU :")
    print("\t\t\t [ 1 ] press 1 for add product name ")
    print("\t\t\t [ 2 ] press 2 for remove product name  ")
    print("\t\t\t [ 3 ] press 3 for view prducts ")
    print("\t\t\t [ 4 ] press 4 for show total product available ")
    print("\t\t\t [ 5 ] press 5 for remove all prodcut ")
    choice = int(input("Enter Your Choice ::  "))
    if choice == 1:
        product_name = input("Enter Product Name : ")
        Product_list.append(product_name)
    elif choice == 2:
        Product_list.remove("Fruits")
    elif choice == 3 :
        print(Product_list)
    elif choice == 4:
        print(len(Product_list))
    elif choice == 5:
        Product_list.clear()
    else:
        print("Operation Is Not Valid..!")
    ch = input("Do You Want To Perform More Operation Press Y For Yes & Press N For No : ")
    if ch == 'Y' or ch == 'y' :
        flag = True
    else:
        flag = False