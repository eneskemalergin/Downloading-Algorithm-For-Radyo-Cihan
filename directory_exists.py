## Function for checking and creating folders.
## Version 0.1
  ## - User must put the path when calling the function as a parameter.
  ## - 
def file_exist(directory):
    import os
    #base_path = input("Please put your file path using the sample form \n C:/user/pc-41/desktop :")
    #directory = base_path + program_name + topic_name      
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("New directory created...")
    else:
        print("You already have specified directory...")