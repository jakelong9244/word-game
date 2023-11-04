def importDictionary():
    # opening the file 
    file_obj = open("dictionary.txt", "r") 
    
    # reading the data from the file 
    file_data = file_obj.read() 

    # splitting the file data into lines 
    dictionary = file_data.splitlines() 

    # closing the file
    file_obj.close() 
    
    return dictionary

def importWordValues():
    # opening the file 
    file_obj = open("letterValues.txt", "r") 
    
    # reading the data from the file 
    file_data = file_obj.read() 
    
    # splitting the file data into lines 
    lines = file_data.splitlines() 

    # initialize dictionary, this will store the point score asssociated with each letter
    wordValues = {}

    # Iterate through each element of the list (each letter and point value), represented by i
    for i in lines:
        # splits the letter and point value and assigns it into a dictionary as the key and value
        letter,value = i.split(",")
        wordValues[letter] = value

    # closing the file
    file_obj.close() 

    return wordValues