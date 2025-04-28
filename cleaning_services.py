print("JB's House Cleaning and Lawn Service\n")

# Create variables for house cleaning prices based on number of rooms

# prices for a small number of rooms
carpet_clean_small = 160
dusting_small = 121
window_cleaning_small = 100
deep_clean_sm = 200

# prices for a medium number of rooms
carpet_clean_medium = 340
dusting_medium = 315
window_cleaning_medium = 280
deep_clean_med = 300

# prices for a large number of rooms
carpet_clean_large = 500
dusting_large = 425
window_cleaning_large = 350
deep_clean_lg = 400

# Prompt user if they'd like house or yard cleaning
house_or_yard_cleaning = input("Would you like (house) or (yard) cleaning services?\n")
house_or_yard_cleaning.lower()

while house_or_yard_cleaning != "house" and house_or_yard_cleaning != "yard" and house_or_yard_cleaning != "h" and house_or_yard_cleaning != "y":
    house_or_yard_cleaning = input("Would you like (house) or (yard) cleaning services?\n")
    house_or_yard_cleaning.lower()


# Create function to calculate the price of the senior discount: 25% off (.25)
def senior_discount(total_cost):
    # Initialize discount percentage
    discount = .25
    # Prompt user for whether they're a senior or not
    qualify_for_discount = input("Are you a Senior? Y or N?\n")
    qualify_for_discount.lower()

    if qualify_for_discount == "y":
        # Calculate the senior discount
        final_cost = total_cost - round((discount * total_cost), 2)

        # Display the final cost of the service with the discount included if a senior
        print(f"You qualify for a discount! You get 25% off.\n")
        print(f"Your final total is ${final_cost}")

    elif qualify_for_discount == "n":
        # Display the final cost of the service with no discount included if not a senior
        print(f"Sorry, you don't qualify for a discount. Your final total is ${total_cost}")
    else:
        quit("Please enter a valid answer.")


# Decide if house cleaning was chosen
if house_or_yard_cleaning == "house" or house_or_yard_cleaning == "h":
    # Display room size qualifications: Small - 1-2 rooms, Medium - 3-4 rooms, Large - 5-6 rooms
    print(
        "As a reminder, our pricing is based on the amount of rooms: Small (1-2 rooms), Medium (3-4 rooms), and large (5-6 rooms)\n")
    # Prompt user for number of rooms
    num_of_rooms = int(input("How many rooms do you have?\n"))

    # Display the cleaning prices based on the user input for the number of rooms

    # small prices: carpet - $160, dusting - $121, windows - 100, deep clean - $200
    if 0 < num_of_rooms < 3:
        num_of_rooms = "small"
        print("For a small number of rooms, our standard prices are:")
        print(f"Cleaning Carpets: ${carpet_clean_small}")
        print(f"Dusting: ${dusting_small}")
        print(f"Window Cleaning: ${window_cleaning_small}")
        print(f"Deep Cleaning is an extra: ${deep_clean_sm}\n")

    # medium prices: carpet - $340, dusting - $315, windows - 280, deep clean - $300
    elif 3 <= num_of_rooms < 5:
        num_of_rooms = "medium"
        print("For a medium number of rooms, our standard prices are:")
        print(f"Cleaning Carpets: ${carpet_clean_medium}")
        print(f"Dusting: ${dusting_medium}")
        print(f"Window Cleaning: ${window_cleaning_medium}")
        print(f"Deep Cleaning is an extra: ${deep_clean_med}\n")

        # large prices: carpet - $500, dusting - $425, windows - 350, deep clean - $400
    elif 5 <= num_of_rooms < 7:
        num_of_rooms = "large"
        print("For a large number of rooms, our standard prices are:")
        print(f"Cleaning Carpets: ${carpet_clean_large}")
        print(f"Dusting: ${dusting_large}")
        print(f"Window Cleaning: ${window_cleaning_large}")
        print(f"Deep Cleaning is an extra: ${deep_clean_lg}\n")
    else:
        quit("Please enter a valid number.")

    # Prompt user for type of cleaning
    cleaning_type = input("What type of cleaning would you like: (Dust)ing, (Window) Cleaning, or (Carpet) Cleaning?\n")
    cleaning_type.lower()

    # Prompt user for condition of cleaning: Standard or Deep Clean
    cleaning_condition = input("Would you like us to do a (stand)ard cleaning or a (deep) clean?\n")
    cleaning_condition.lower()


    # Create function to calculate the price of cleaning rooms
    def cleaning_service(num_of_rooms, cleaning_type):

        # Set prices based on number of rooms and type of cleaning done
        if num_of_rooms == "small" and cleaning_type == "carpet":
            cleaning_price = carpet_clean_small
        elif num_of_rooms == "small" and cleaning_type == "dust":
            cleaning_price = dusting_small
        elif num_of_rooms == "small" and cleaning_type == "window":
            cleaning_price = window_cleaning_small

        elif num_of_rooms == "medium" and cleaning_type == "carpet":
            cleaning_price = carpet_clean_medium
        elif num_of_rooms == "medium" and cleaning_type == "dust":
            cleaning_price = dusting_medium
        elif num_of_rooms == "medium" and cleaning_type == "window":
            cleaning_price = window_cleaning_medium

        elif num_of_rooms == "large" and cleaning_type == "carpet":
            cleaning_price = carpet_clean_large
        elif num_of_rooms == "large" and cleaning_type == "dust":
            cleaning_price = dusting_large
        elif num_of_rooms == "large" and cleaning_type == "window":
            cleaning_price = window_cleaning_large

        else:
            quit("I'm sorry, we don't offer that service.")

        # Calculate final cleaning price based on if deep cleaning was requested
        if cleaning_condition == "deep":
            if num_of_rooms == "small":
                return cleaning_price + deep_clean_sm
            elif num_of_rooms == "medium":
                return cleaning_price + deep_clean_med
            elif num_of_rooms == "large":
                return cleaning_price + deep_clean_lg
        elif cleaning_condition == "stand" or cleaning_condition == "standard":
            return cleaning_price
        else:
            quit("Please enter a valid response.")


    total_cost = cleaning_service(num_of_rooms, cleaning_type)
    # Display the total cleaning cost
    print(f"The total to clean your home is ${total_cost}\n")

    # Call senior discount function to decide if a discount should be applied
    senior_discount(total_cost)

# Decide if yard cleaning was chosen
elif house_or_yard_cleaning == "yard" or house_or_yard_cleaning == "y":
    # Initialize prices for mowing: .50 per square foot, edging: 5 per linear foot, and shrub pruning: 10 per shrub
    mowing_price = .50
    edging_price = 5
    pruning_price = 10

    # Display yard service prices
    print("Our prices are:")
    print(
        f"Mowing: ${mowing_price}/square foot, Edging: ${edging_price}/linear foot, and Shrub Pruning: ${pruning_price}/shrub\n")

    # Prompt user for type of yard service they'd like done
    service_type = input("Would you like mowing, edging, or shrub pruning done?\n")
    service_type.lower()


    # Create function to calculate the price of yard work
    def yard_service(service):
        # Decide if mowing was chosen
        if service == "mowing" or service == "m":
            # Prompt user for length of yard in feet
            yard_length = float(input("How many feet is the length of your yard?\n"))
            # Prompt user for width of yard in feet
            yard_width = float(input("How many feet is the width of your yard?\n"))

            # Calculate square footage of yard
            square_feet = yard_length * yard_width

            # Calculate total cost of mowing
            total_cost = square_feet * mowing_price

            # Display measurement and total cost of mowing
            print(f"With a square footage of {square_feet}ft, your total is ${total_cost}.\n")

            # Call senior discount function to decide if a discount should be applied
            senior_discount(total_cost)

        # Decide if edging was chosen
        elif service == "edging" or service == "e":
            # Prompt user for linear footage of yard's edges
            edging_length = float(input("What is the linear footage of your yard's edges?\n"))

            # Calculate cost of edging the yard
            total_cost = edging_length * edging_price

            # Display the linear footage of the yard and the total cost of edging
            print(
                f"The linear footage of your edges was {edging_length}ft. The cost of edging your yard is ${total_cost}.\n")

            # Call senior discount function to decide if a discount should be applied
            senior_discount(total_cost)

        # Decide if pruning was chosen
        elif service == "shrub" or service == "pruning" or service == "s" or service == "p":
            # Prompt user for the number of shrubs they'd like pruned
            num_of_shrubs = int(input("How many shrubs would you like pruned?\n"))

            # Calculate the total cost of pruning
            total_cost = num_of_shrubs * pruning_price

            # Display the number of shrubs they'd like pruned and the total cost of pruning
            print(f"You would like {num_of_shrubs} shrub(s) pruned. Your total is ${total_cost}.\n")

            # Call senior discount function to decide if a discount should be applied
            senior_discount(total_cost)


    yard_service(service_type)







