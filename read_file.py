#Rread file and convert to list
def read_file(filename: str) -> list[int]:
    """
    Reads a file and returns a list of integers.

    Args:
        filename (str): The name of the file to read.
    Returns:
        data (list): A list of integers from the file.
    """
    # Open the file
    # Read the file
    f=open(filename,"r")

    s=f.read()
    numbers= s.split(",")
    i=0
    while i < len(numbers):
        numbers[i]=int(numbers[i])
        i+=1

    return numbers 

print(read_file("data.txt"))

#Print list from file

