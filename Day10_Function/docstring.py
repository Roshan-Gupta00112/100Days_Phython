def format_name(f_name, l_name):
    """The function will convert the name to title which means
                the first letter of each word
                will be in the capital in the output

                The description in the docstrings will be displayed
                if you move the cursor where you are calling the function

                The docstring will be displayed as function definition
                on either using single or double quotation marks

                It will not displayed if you comment out approach"""

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)