shopping_list = []
def display_menu():
     print("Shopping List Manager")
     print("1. Add an item")
     print("2. Remove an item")
     print("3. View the list")
     print("4. Exit")


def add_item(shopping_list):
    item = input("Enter the name of item:")
    shopping_list.append(item)
    print(item, "added successfully")

def remove_item(shopping_list):
        item = input("Enter the name of the item")
        for item in shopping_list:
              if item:
                 shopping_list.remove(item)
                 return
        print(item, "not found!") 

def view_item(shopping_list):
     for item in shopping_list:
          if item:
               print("Item_name:", item)  
               return
     print(name, "not found!")  
                    
                 
              
       
              
    


        
        

