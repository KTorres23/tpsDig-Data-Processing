# Purpose: Retrieve and manipulate tpsDIG data for MorphoJ analysis input.
# Created by Karina Torres; torresk@ufl.edu
# Last updated May 20, 2024

# Program function:
# - Open .tps file
# - Replace all spaces with tabs
# - Replace ID= with @ID=
# - Replace Image= with unique specimen identifier, described as the Unique Identifier Code (UIC)
#   > search for ID# using endswith(listIDnum[x])
#   > if endswith() returns true, then rename image= with that [x] index
#       corresponding to the UIC[x]
#   > get UIC from "Official-UICs-CleanedData.txt"
# - Save file as .txt file



import os

def main():

    UICsList = []

# Opens file for data processing
    inputfileName = input("What is the name of the .tps file containing" +
                          "\nthe landmark data? ")

    outputfileName = inputfileName
    inputfileName = inputfileName + ".tps"

    # ---------------------------------------------------- TO DO ----------------------------------------------------
    # Enter the file path to the folder where your .TPS files are stored
    # ---------------------------------------------------- TO DO ----------------------------------------------------
    inputfileName = "C:\\Users\\.......\\" + inputfileName

    with open(inputfileName, "r") as inputFile:
        lines = inputFile.readlines()

# ---------------------------------------------------- IMPORTANT ----------------------------------------------------
# The following lines accesses the UICs for your data. Your file with the specimen data should be named as the
# following: "OFFICIAL-UICs-CleanedData.txt". Otherwise, change the string below.
# ---------------------------------------------------- IMPORTANT ----------------------------------------------------

# Opens file with UICs
    with open("OFFICIAL-UICs-CleanedData.txt", "r") as UICsFile:
        UICsLines = UICsFile.readlines()

# Creates a list of UICs
    for line in UICsLines:
        line = line.rstrip()
        UICsList.append(line)


# Creates file with updated data
    outputfileName = "MorphoJ input - " + outputfileName + ".txt"

    # ---------------------------------------------------- TO DO ----------------------------------------------------
    # Enter the file path to the folder where you will stored your .txt file datasets for MorphoJ analysis
    # ---------------------------------------------------- TO DO ----------------------------------------------------
    outputfileName = "C:\\Users\\........\\" + outputfileName

    # Use x to create a new file
    # x will not rewrite over a file
    # w will rewrite over the file
    outputFile = open(outputfileName, "x")

    counter = 0

    # Manipulates data for MorphoJ processing
    for line in lines:
        
        # Changes to UIC name for MorphoJ reading
        if "IMAGE=" in line:

            # Splits path into a list
            line = line.split("_")

            # Uses last list index which should contain specimen#.jpg
            # Strips newline, removes .jpg trail, and adds zeros as in UICs
            line = line[len(line) - 1].rstrip("\n")

            if ".jpg" in line:
                line = line.rstrip(".jpg")

            else:
                print("\n\n\nError occurred with finding" +
                      " the specimen number.\n\n\n")

            while True:
                if len(line) < 4:
                    line = "0" + line

                else:
                    break

            for x in range(len(UICsList)):
                UIC = UICsList[x]
                UIC = UIC[7:11]

                if line == UIC:
                    line = "Image=" + UICsList[x] + "\n"
                    break
                else:
                    pass



        # Removes reading of irrelevant ID=## in MorphoJ
        elif "ID=" in line:
            line = line.replace("ID", "@ID")

            

        # Ensures there are 7 landmarks in the data
        elif "LM=" in line:
            if "LM=7" not in line:
                print("\n\n-----------------------------------------------------------------" +
                      "\n    ERROR: THE FOLLOWING LINE HAS LANDMARKS NOT EQUAL TO 7!!!" +
                      "\n     Be sure to remove these specimen or mark the landmarks:\n", end="")
                print(lines[counter+1], end="")
                print("-----------------------------------------------------------------")

            else:
                pass
        


        # Replaces spaces to tabs
        elif " " in line:
            line = line.replace(" ", "\t")



        else:
            pass


       
        outputFile.write(line)
        counter += 1
        
    outputFile.close()

    
    print("\n\n\tThe file for MorphoJ processing has been" +
          "\n\t    created in the following file:\n" +
          outputfileName)


# Exits the program when user is ready
    while True:
        x = input("\nHit Enter to exit")
        if not x :
            print("Exiting the program...")
            break

        else:
            continue
                    
    

main()
