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
        print("### 3. Types of Post's Performance Throughout the Day")
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



def total_interaction_menu():
    df = pd.read_csv("Task4a_data.csv")

    flag = True
    while flag:
        
        post_types = ['Image', 'Poll', 'News/update', 'Advertisement']

        print("#################################################")
        print("############### Total Interaction ###############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        # automates printing options
        for post in post_types:
            print(f"### {post_types.index(post)+1}. {post}") 

        # tuple contains the numbers that have an option assigned to them
        num_choices = ('1', '2', '3', '4')
        
        choice = input('Enter your number selection here: ')

        # checks that the option they have selected is in the 'choices' tuple
        if choice not in num_choices:
            print("Please enter an option from above")
            flag = True
        else:    
            print('Choice accepted!')
            # converts choice into the words for filtering
            choice = int(choice)
            return post_types[choice-1]


# uses the choice made from 'average_menu' to filter the csv file turned dataframe
def get_avg_data(avg_choice):
    df = pd.read_csv("Task4a_data.csv")

    # groups the df by date, with the mean of the avg_choice being the filter
    extract = df.groupby(['Date'], as_index=False) [avg_choice].mean()
    extract_no_index = extract.to_string(index=False)
    
    # outputs the data with columns 'Date' and avg_choice
    print(f"Here is the average number of {avg_choice} each day during the campaign:")
    print(extract_no_index)


def get_post_interaction_data(post_type):
    df = pd.read_csv("Task4a_data.csv")
    fig, ax = plt.subplots(layout='constrained')


    # creates new column with total likes, shares and comments for each day
    df['Total Interactions'] = df[['Likes', 'Shares', 'Comments']].sum(axis=1)
    
    # extracts data by post type
    extract_types = df.loc[df['Post Type'] == post_type]

    # groups extracted data by date and sums the total interaction by day
    extract = extract_types.groupby(['Date']) ['Total Interactions'].sum()

    print(f'Here is the total interactions for the {post_type} post type on days they were used:')
    print(extract.to_string())
        
    # plotting the graph
    plt.plot(extract, marker='x')
    plt.xticks(rotation=50)
    plt.xlabel('Date')
    plt.ylabel('Interactions')
    plt.title(f'Total interactions for {post_type} post type')
    plt.show()

# main program loop 
def main():
    flag = True
    while flag:
        main_menu_choice = main_menu()

        if main_menu_choice == "1":
            avg_choice = average_menu()
            get_avg_data(avg_choice)
            
        elif main_menu_choice == "2":
            post_type = total_interaction_menu()
            get_post_interaction_data(post_type)

        elif main_menu_choice == 'x':
            print('Exiting...')
            flag = False

main()




