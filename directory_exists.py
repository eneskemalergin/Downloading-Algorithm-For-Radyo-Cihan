## Function for checking and creating folders.
## Version 0.2.1
  ## - Parameters:
  ##    * base_url
  ##    * topic_name
  ##    * program_name
  ## It creates a folders with topic_name, and program_name
def directory_exist_V2(base_url, program_name, topic_name):
    import os
    # Checks the first path of a directory.
    directory_one  = base_url + '/' + program_name  
    if not os.path.exists(directory_one):
        os.makedirs(directory_one)
        print("New directory created...")
    else:
        print("You already have specified directory...")
    
    # Checkst the second level path of a directory.
    directory_two = directory_one + '/' + topic_name 
    if not os.path.exists(directory_two):
        os.makedirs(directory_two)
        print("New directory created...")
        return(directory_two)
    else:
        print("You already have specidied directory...")                 
        return(directory_two) 