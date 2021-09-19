import os

req_path=input("Enter your directory Path ")

if os.path.isfile(req_path):
    print (f"The given path {req_path} is a file. Please pass only directory path")
else:
    all_files=os.listdir(req_path)
    if (all_files)==0:
        print(f"The given path is {req_path} an empty path")
    else:
        req_extension=input("Enter the required files extention .py/.sh/.log/.txt:  ")
        req_files=[]
        for each_file in all_files:
            if each_file.endswith(req_extension):
                req_files.append(each_file)
        if len(req_files)==0:
            print(f"There are no {req_extension} files in the logcation of {req_path}")
        else:
            print(f"There are {len(req_files)} files in the location of {req_path} with an extention of {req_extension}")
            print(f"So, the files are: {req_files}")