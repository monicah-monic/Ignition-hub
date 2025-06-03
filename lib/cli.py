def main():
    from main import create_customer, fetch_customers, fetch_customer_by_id, update_customer,delete_customer, create_car, fetch_cars,fetch_car_by_id,update_car, delete_car
    from main import create_car_rental, fetch_car_rentals, fetch_car_rental_by_id, update_car_rental, delete_car_rental

    while True:
        print()
        print("\033[95mWelcome to Ignition Hub\033[0m")
        print()
        print("1. Manage Customers")
        print("2. Manage Cars")
        print("3. Manage car rentals")
        print()
             
        main_choice = input("Enter your choice: ")

        if main_choice == "1" :
            print("===============Manage customers================")
            print("1. Create customer")
            print("2. List customer") 
            print("3. List customer by id")   
            print("4. Update Customer")
            print("5. Delete Customer")
            print("0. Exit")
        
            choice = input("Enter your choice: ")
            print()
            if choice == "1":
                create_customer()
            elif choice == "2":
                fetch_customers()
            elif choice == "3":
                fetch_customer_by_id()
            elif choice == "4":
                update_customer()
            elif choice == "5":
                delete_customer() 
            elif choice == "0":
                print("\033[95mBye! Bye!\033[0m")
                break   
            else:
                print("\033[95mInvalid input!Try again[0m")    

        if main_choice == "2" :
            print("===============Manage cars================")
            print()
            print("1. Create car")
            print("2. List cars") 
            print("3. List car by id")   
            print("4. Update Car")
            print("5. Delete Car")
            print("0. Exit")

            choice = input("Enter your choice: ")
            print()
            if choice == "1":
                create_car()
            elif choice == "2":
                fetch_cars()
            elif choice == "3":
                fetch_car_by_id()
            elif choice == "4":
                update_car()
            elif choice == "5":
                delete_car()
            elif choice == "0":
                print("\033[95mBye! Bye!\033[0m")
                break   
            else:
                print("\033[95mInvalid input!Try again[0m")          


        if main_choice == "3" :
            print("===============Manage car hire================")
            print("1. Create car rental")
            print("2. List cars rented") 
            print("3. List car rented  by id")   
            print("4. Update Car rented")
            print("5. Delete Car rented")
            print("0. Exit")
            
            choice = input("Enter your choice: ")
            print()
            if choice == "1":
                create_car_rental()
            elif choice == "2":
                fetch_car_rentals()
            elif choice == "3":
                fetch_car_rental_by_id()
            elif choice == "4":
                update_car_rental()
            elif choice == "5":
                delete_car_rental()    
            elif choice == "0":
                print("\033[95mBye! Bye!\033[0m")
                break   
            else:
                print("\033[95mInvalid input!Try again[0m") 


if __name__ == "__main__":
    main()