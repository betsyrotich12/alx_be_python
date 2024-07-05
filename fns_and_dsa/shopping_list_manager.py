shopping_list = []
def display_menu():
     print("Shopping List Manager")
     print("1. Add Item")
     print("2. Remove Item")
     print("3. View List")
     print("4. Exit")


def add_item(shopping_list):
    item = input("Enter the item to add:")
    shopping_list.append(item)
    print(item, "added successfully")

def remove_item(shopping_list):
        item = input("Enter the item to remove")
        for item in shopping_list:
              if item:
                 shopping_list.remove(item)
                 return
        print(item, "not found!") 

def view_item(shopping_list):
     if shopping_list:
          print("\nCurrent shopping list:")
     for item in shopping_list:
        print(item)  
        return
     print(item, "not found!")
                    
                 
              
       
              
    


        
        

