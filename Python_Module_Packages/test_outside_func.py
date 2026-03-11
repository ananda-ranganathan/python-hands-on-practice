from python_custom_user_packages.maths_calc_custom_func import * # importing package

from python_custom_user_packages.python_sub_packages.sub_maths_func import sub_maths_cust_func # importing sub package
print(add_2_nums(2,3))
print(multi_custom_func(2,47))


print(sub_maths_cust_func(34,2,5))

# Important to Access the File in Command Prompt
# CD to the parent folder - Python_Module_Packages> cd Python_Module_Packages> python test_outside_func.py

# (C:\Users\anand\zen_python_lang_hands_on_ds\venv) C:\Users\anand\zen_python_lang_hands_on_ds\Python_Module_Packages\Python_Module_Packages>python test_outside_func.py
# 5
# 94


# test_outside_func.py file Running in Command Prompt
# this file is located outside the package folder --> 
# (C:\Users\anand\zen_python_lang_hands_on_ds\venv) C:\Users\anand\zen_python_lang_hands_on_ds\Python_Module_Packages>
# Type the cmd command
#(C:\Users\anand\zen_python_lang_hands_on_ds\venv) C:\Users\anand\zen_python_lang_hands_on_ds\Python_Module_Packages>python test_outside_func.py
# output :5
# Output :6

# (C:\Users\anand\zen_python_lang_hands_on_ds\venv) C:\Users\anand\zen_python_lang_hands_on_ds\Python_Module_Packages>python test_outside_func.py
# 5
# 94

# (C:\Users\anand\zen_python_lang_hands_on_ds\venv) C:\Users\anand\zen_python_lang_hands_on_ds\Python_Module_Packages>


# Important to Access the File in Command Prompt
# Whereas, the file is located inside the package folder --> test.py file and test_inside_func.py file will not run says FileNotFoundError
# to run the file we need to go to the folder where the file is located and run the file
# i.e., the test.py file and test_inside_func.py file should directly created under the parent folder - Python_Module_Packages

