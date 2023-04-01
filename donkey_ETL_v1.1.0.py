import os #check file in OS
import csv
from datetime import datetime

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# V1.0.1 - reduce task, count lind function and get gl line
# previous version GET lines to DATA_List, then GET_GL_line function looping by DATA_List
# this version, GET only howmany lines in text file, then using range() for looping instead of DATA_list

# V1.0.2 - get INPUT file name form GUI input
# previous version - hard code file name 

# V1.0.3 - CHECK if GET GL_Line = 0, no GLcode found -> exit()
# previous version - running to the end even no GLcode found

# V1.0.4 - GET very columns in GL_code line

# V1.0.5 - slit like V1.0.4 does not work, column 2 GL name was split
# fix by column 1 and 2 by fix width, then other columns using slit function
# modify string before transform to CSV


# --------------------------------
# Function Section
# --------------------------------
# mainFunction
# sub_function

def check_INPUT_file_exist(filename):
    # Call function Check is File exist
    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'Call function Check is File exist'
    print (logtime,':',log_message)

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = ' - Target file : ' + filename
    print (logtime,':',log_message)


    # Start Function
    #--------------------------
    if os.path.isfile(filename):
        print(logtime,':',' - file exists')
    else:
        print(logtime,':',' - file does not exist')
        quit()

    #--------------------------
    # END Function
    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'End function Check is File exist'
    print (logtime,':',log_message)


def get_GL_Lines(filename):
    # Call function GET GL-Lines in file
    # - count total lines in file
    # - GET only line that has GL_code

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'Call function GET GL-Lines in file'
    print (logtime,':',log_message)

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = ' - Target file : ' + filename
    print (logtime,':',log_message)

    # Start Function
    #--------------------------
    line = []
    targetLines_list = []

    with open(filename, 'r') as file:
        contents = file.readlines()
        total_lines = len(contents)

        file.close()



    # LOOP for finding lines that contain GL_Code, file not header
    with open(filename, 'r') as file:
        for i in range(total_lines):
            line = file.readline()

            GL_set1 = line[str_index_GL_set1_start:str_index_GL_set1_end]
            GL_set2 = line[str_index_GL_set2_start:str_index_GL_set2_end]

            is_GL_Line = GL_set1 + GL_set2

            if is_GL_Line.isdigit():
                targetLines_list.append(i)

        file.close()

    if len(targetLines_list) == 0:
        logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = ' - Total lines ' + str(total_lines) + ' rows'
        print (logtime,':',log_message)

        logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = 'no GL_Code found, END program'
        print (logtime,':',log_message)

        quit()

    #--------------------------
    # END Function
    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = ' - Total lines ' + str(total_lines) + ' rows'
    print (logtime,':',log_message)

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = ' - Found GL_code ' + str(len(targetLines_list)) + ' rows'
    print (logtime,':',log_message)

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'End function GET GL-Lines in file'
    print (logtime,':',log_message)


    return targetLines_list


def read_specific_lines(filename, line_numbers):
    # Call function GET Spacific Lines
    # - line_numbers : List[]

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'Call function GET Spacific Lines'
    print (logtime,':',log_message)

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = ' - Target file : ' + filename
    print (logtime,':',log_message)

    # Start Function
    #--------------------------

    with open(filename, 'r') as file:
        lines = []
        for i, line in enumerate(file):
            if i in line_numbers:
                lines.append(line)
    file.close()

    #--------------------------
    # END Function
    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = ' - GET ' + str(len(lines)) + ' rows'
    print (logtime,':',log_message)

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'End function GET Spacific Lines'
    print (logtime,':',log_message)

    return lines


def check_OUTPUT_file_exist(fileName):
    # Call function CHECK file exist

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'Call function CHECK file exist'
    print (logtime,':',log_message)

    # Start Function
    #--------------------------

    if os.path.exists(fileName):
        #delete previous file
        os.remove(fileName)

        logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = ' - file ' + OUTPUT_file_name + ' exist' 
        print (logtime,':',log_message)

        logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = ' - DELETE ' + OUTPUT_file_name
        print (logtime,':',log_message)

    else:
        logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = ' - file ' + OUTPUT_file_name + ' doesn''t exist' 
        print (logtime,':',log_message)

    #--------------------------
    # END Function
    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'End function CHECK file exist'
    print (logtime,':',log_message)

def writing_CSV(OUTPUT_file,USALI):
    # Call function WRITE to CSV

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'Call function WRITE to CSV'
    print (logtime,':',log_message)

    # Start Function
    # split function doesn't work with Thai text in description column,
    # So Fix width has to apply to GL and text column, before using slipt function.
    #--------------------------
    i=0
    for writing_item in USALI:
        i += 1
        with open(OUTPUT_file, 'a',encoding='utf-8',newline='') as file_object:
            lines = csv.writer(file_object)
            
            # TRANFORM - modify each column
            gl_account = writing_item[0:10]
            gl_account = gl_account.strip()                 # remove white space
            gl_account = gl_account.replace('"', '')        # remove ""

            gl_name = writing_item[11:80]
            gl_name = gl_name.strip()                       # remove white space

            gl_amount = writing_item[80:180]
            gl_amount_split = gl_amount.split()             # saperate columns by ","

            # grouping column back
            writingrow = [gl_account]
            writingrow.append(gl_name)
            writingrow.extend(gl_amount_split)
            
            lines.writerow(writingrow)


    #--------------------------
    # END Function
    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = ' - WRITE CSV ' + str(i) + ' rows'
    print (logtime,':',log_message)

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = ' - Generate file ' + OUTPUT_file_name + ' successful'
    print (logtime,':',log_message)

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'End function WRITE to CSV'
    print (logtime,':',log_message)


def extractingFile():
    # Initiate main function - Extracting File
    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'Initiate main function - Extracting File'
    print (logtime,':',log_message)

    # Start MAIN Function
    #--------------------------
    # EXTRACT
    INPUT_file_name = entFileName.get() + '.TXT'
    INPUT_file_dir = os.path.dirname(os.path.realpath(__file__))
    INPUT_file = os.path.join(INPUT_file_dir, INPUT_file_name)

    OUTPUT_file_name = OUTPUT_Prefix + INPUT_file_name
    OUTPUT_file = os.path.join(INPUT_file_dir, OUTPUT_file_name)

    # - CHECK : Input file exist
    #   - ERROR handle
    check_INPUT_file_exist(INPUT_file)

    # - GET : only lines that contain GL account
    GlLines_list = get_GL_Lines(INPUT_file)

    # - GET : GL account and amount
    dataInGlLines_list = read_specific_lines(INPUT_file, GlLines_list)

    # - GET : GL_code and value_amount from spacific lines
    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'GET GL_code and value_amount from spacific lines'
    print (logtime,':',log_message)


    # - CHECK : Output file exist, if it's exist, delete it.
    #   - writing will append at the end of the file
    check_OUTPUT_file_exist(OUTPUT_file)

    # LOAD
    writing_CSV(OUTPUT_file,dataInGlLines_list)

    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = 'END main function - Extracting File'
    print (logtime,':',log_message)


# --------------------------------
# GUI Section
# --------------------------------
title="Donkey ETL"

backgroundColor = "#7EA8BE"
textColor = "white"
font="Anupan"


main_window = Tk()
main_window.title('Donkey ETL v1.0.1')
main_window.geometry('400x300')
main_window.config(bg=backgroundColor)


H1 = Label(main_window, text=title,font=( font + " Bold", 30),bg=backgroundColor,fg=textColor)
H1.grid(row=0,column=0,columnspan=4,sticky="W",padx=50, pady=5)

H2_lottery = Label(main_window, text="Extract file for USALI report",font=(font, 14),bg=backgroundColor,fg=textColor)
H2_lottery.grid(row=1,column=0,columnspan=8, sticky="W",padx=50,pady=10)


lblFileName = Label(main_window, text="FIle Name",bg=backgroundColor,fg=textColor)
lblFileName.grid(row=2,column=1,sticky="E",padx=5, pady=5)

entFileName= Entry(main_window)
entFileName.insert(0,'GLTRIAL')
entFileName.grid(row=2,column=2,sticky="W")


B1_submit = ttk.Button(main_window,text="Gen USALI",command= extractingFile)
B1_submit.grid(row=4,column=1,sticky="E",padx=5, pady=10)


# --------------------------------
# Main Parameter
# --------------------------------
INPUT_file_name = ''
INPUT_file_dir = ''
INPUT_file = ''

# Parameter to slide GL-code, example 4100-00
str_index_GL_set1_start = 1
str_index_GL_set1_end = 5

str_index_GL_set2_start = 6
str_index_GL_set2_end = 8

# OUTPUT file
OUTPUT_Prefix = 'donkey_'
OUTPUT_file_name = ''
OUTPUT_file = ''



# --------------------------------
# Main Program
# running when initiate program
# --------------------------------



# -------------------------
# Start the main event loop
main_window.mainloop()



