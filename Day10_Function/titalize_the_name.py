# 1st Approach
import inspect

def is_name_valid(name):
    if name == "" or name == " ":
        return False
    else:
        return True


def title_using_upper_fn(part_name):
    part_name_list = list(part_name)
    # TC = O(N)
    # SC = O(N)

    part_name_list[0] = part_name_list[0].upper()

    formatted_part_name = "".join(part_name_list)
    #  TC = O(N)

    return formatted_part_name

# 2nd Approach
def title_using_title_fn(part_name):
    return part_name.title()  # TC = O(N)



# def format_using_upper_fn(f_name, l_name):
#     formatted_f_name = title_using_upper_fn(f_name)
#     formatted_l_name = title_using_upper_fn(l_name)
#     print(f"Your Name is: {formatted_f_name} {formatted_l_name}")
#
#
#
# def format_using_title_fn(f_name, l_name):
#     formatted_f_name = title_using_title_fn(f_name)
#     formatted_l_name = title_using_title_fn(l_name)
#     print(f"Your Name is: {formatted_f_name} {formatted_l_name}")



def format_using_upper_fn(f_name, l_name):
    is_f_name_valid = is_name_valid(f_name)
    is_l_name_valid = is_name_valid(l_name)

    if not is_f_name_valid and not is_l_name_valid:
        return print("Please! provide first name and last name")

    formatted_f_name = title_using_upper_fn(f_name)
    formatted_l_name = title_using_upper_fn(l_name)
    print(f"Method: {inspect.currentframe().f_code.co_name} → Your Name is: {formatted_f_name} {formatted_l_name}")


def format_using_title_fn(f_name, l_name):
    is_f_name_valid = is_name_valid(f_name)
    is_l_name_valid = is_name_valid(l_name)

    if not is_f_name_valid and not is_l_name_valid:
        return print("Please! provide first name and last name")

    formatted_f_name = title_using_title_fn(f_name)
    formatted_l_name = title_using_title_fn(l_name)
    print(f"Method: {inspect.currentframe().f_code.co_name} → Your Name is: {formatted_f_name} {formatted_l_name}")




# format_using_upper_fn("roshan", "Gupta")

# format_using_upper_fn("roshan", "")
# format_using_upper_fn("", "Gupta")
# The above two will throw an error because of an empty list

# format_using_upper_fn("", "")


format_using_title_fn("rosHan", "KUMAR")
format_using_title_fn("", "KUMAR")
format_using_title_fn("rosHan", "")
format_using_title_fn("", "")