import pandas as pd
import matplotlib.pyplot as plt


# menu to select an option to filter CSV file
def main_menu():
    flag = True
    while flag:
        print("#################################################")
        print("############## Snowy Animal Rescue ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average Social Media Interaction Data")
        print("### 2. Types of Post that get the Most Interactions")
        print("### or 'x' to exit the program")

        # tuple contains the numbers (or letter) that have an option assigned to them
        choices = ('1', '2', '3', 'x')

        choice = input('Enter your number selection here: ')

        # checks that the option they have selected is in the 'choices' tuple
        if choice not in choices:
            print("Please enter an option from above")
            flag = True
        else:    
            print('Choice accepted!')
            return choice

    

# menu to select an option of likes, shares or comments 
# For option no. 1 in the 'main_menu' function
def average_menu():
    flag = True
    while flag:
        print("#################################################")
        print("############## Average Interaction ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average number of Likes")   
        print("### 2. Average number of Shares") 
        print("### 3. Average number of Comments")  

        # tuple contains the numbers that have an option assigned to them
        num_choices = ('1', '2', '3')
        str_choices = ('Likes', 'Shares', 'Comments')

        choice = input('Enter your number selection here: ')

        # checks that the option they have selected is in the 'choices' tuple
        if choice not in num_choices:
            print("Please enter an option from above")
            flag = True
        else:    
            print('Choice accepted!')
            # converts choice into the words for filtering
            choice = int(choice)
            return str_choices[choice-1]



# uses the choice made from 'average_menu' to filter the csv file turned dataframe
def get_avg_data(avg_choice):
    df = pd.read_csv("Task4a_data.csv")

    # groups the df by date, with the mean of the avg_choice being the filter
    extract = df.groupby(['Date'], as_index=False) [avg_choice].mean()
    extract_no_index = extract.to_string(index=False)
    
    # outputs the data with columns 'Date' and avg_choice
    print(f"Here is the average number of {avg_choice} each day during the campaign:")
    print(extract_no_index)
   

# main program loop 
def main():
    flag = True
    while flag:
        main_menu_choice = main_menu()

        if main_menu_choice == "1":
            avg_choice = average_menu()
            get_avg_data(avg_choice)
            

        elif main_menu_choice == 'x':
            print('Exiting...')
            flag = False

main()



