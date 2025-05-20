email_input = input("Enter your email address: ")

def email_checker(e):
    list_of_ends = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
    index_at = 0
    index_dot = 0
    count_dot = 0
    count_at_therate = 0
    after_at = ""
    
    if "@" in e and "." in e:
        count_at_therate = e.count("@")
        count_dot = e.count(".")
        if(count_at_therate > 1 or count_dot < 1):
            print("Invalid email address.")
            print("An email should contain exactly one '@' and at least one '.'")
            print("Please try again.")
        else:
            index_at = e.find("@") + 1
            index_dot = e.find(".") + 1
            after_at = e[index_at: len(e)]
            # print("@ found at index", e.find("@")+1)
        if(e.find("@") + 1 > 2):
            for i in list_of_ends:
                if(i in after_at):
                    print("Email domain recognized. Validation successful.")
                    break
            else:
                print("Unrecognized email domain. Please use a valid provider such as Gmail, Hotmail, Yahoo, or Outlook.")
        else:
            print("Invalid email address.")
            print("The email username is too short. It must contain more than two characters before '@'.")
    else:
        print("Invalid email format.")
        print("An email address must contain both '@' and '.' characters.")

    print("Index of '@':", index_at)
    print("Index of '.':", index_dot)
    print("Total '.' count:", count_dot)

email_checker(email_input)
