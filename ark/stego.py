import cv2
import os
import string
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def main():
    while True:
        print("\nChoose option to perform")
        print("1. Encrypt data to stego image")
        print("2. Decrypt data from a stego image")
        print("0. exit")
        choice = int(input("Write option: "))
        global asc #used to make them global
        global num
        asc={}#maps char with ascii values
        num={} #maps ascii value with chars
        for i in range(256): #maps all chars
            asc[chr(i)]=i
            num[i]=chr(i)
        if choice==1:  #encryption of stego image and its pixel location data
            img = input("Enter the image name along with extension: ")
            image = cv2.imread(img)
            height, width, channel = image.shape
            
            #secret_key generation for encryption of key_string
            secret_key_choice=int(input("\nChoose an option\n1.Custom key Encryption\n2.Random key encryption(key will be randomly generated and provided):\n "))
            if secret_key_choice==1:
                while True:
                    secret_key=input("Enter your 16 digit key: ")
                    if len(secret_key)==16:
                        break
                    else:
                        print("Encryption can only be done with a 16 digit key , please enter one with same size")
            elif secret_key_choice==2:
                secret_key=generate_random_key()
                print("Your secret key is: ", secret_key)
                 
            Encrypt_stego_image(image , secret_key)#encodes the image with our data and encrypts the string of locations where its stored
            
        elif choice==2:
            img = input("Enter the image name along with extension: ")
            secret_key=input("Enter the secret key for decryption: ")
            image = cv2.imread(img)
            Decrypt_stego_image(image , secret_key)
        else:
            break

def Encrypt_stego_image(image, secret_key):
    message = input("Enter the message you want to encrypt: ")
    location = []  # stores the row/col value for the pixel where data is stored
    
    height, width, channel = image.shape  # used to make sure rows and col don't go out of bounds by height for rows and width for col
    bgr = 0  # channel=3 as by default cv2 reads in bgr format 0=blue,1=green,2=red
    
    for i in range(len(message)):
        # generates random location of pixels
        random_row = random.randint(0, height)
        random_col = random.randint(0, width)
        # encodes the stego image as per random locations
        image[random_row, random_col, bgr] = asc[message[i]]
        # stores the row and col value of that pixel as a tupple in list key
        location.append((random_row, random_col))
        bgr = (bgr + 1) % 3  # selects which value to encode next

    # print("location: ",location) # debugging line

    # converts the location tupples into a string to be encrypted 
    location_string = " ".join([f"{row} {col}" for row, col in location])
    #print("key string: ", location_string) #debugging line to check tuple conversion to string is happening
    #print(len(location_string))  # length includes individual elements and spaces as in string all of them are considered as elements

    location_string_cipher = encrypt_message(location_string, secret_key)  # used to encrypt the string of location 

    print("Your Encrypted Location Cipher Text: ", location_string_cipher)
    #print(len(location_string_cipher)) Debugging line
    
    
    #cv2.imwrite("encrypted.png", image)
    print("Encrypted sucesssfully")
    save_data(image, secret_key, location_string_cipher)
    # os.system("start encrypted.png")  # can be used to open and verify stego image
   

def pad(text):
    """Pads the text to be a multiple of 16 bytes for AES encryption."""
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def encrypt_message(message, secret_key):
    """Encrypts a message using AES encryption."""
    key = secret_key.ljust(16)[:16].encode("utf-8")  # Ensure 16-byte key
    iv = get_random_bytes(16) #this ensures that if the same cipher is encrypted again it has some randomness to prevent steganalysis
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_bytes = cipher.encrypt(pad(message).encode("utf-8"))
    return base64.b64encode(iv + encrypted_bytes).decode("utf-8")

def generate_random_key(length=16):
    """
    Generates a random key of length 16 for AES encryption using numerals and alphabets.
    """
    # Define the character pool: digits (0-9) + uppercase letters (A-Z) + lowercase letters (a-z)
    characters = string.digits + string.ascii_letters
    # Randomly select characters from the pool
    random_key = ''.join(random.choice(characters) for _ in range(length))
    return random_key

def save_data(image, secret_key, ciphertext):
    """ poouch  user say kaha save krna hai  image, key, and ciphertext """
    
    choice = input("Would You like to save the encryption in same directory? (y/n): ").strip().lower()
    
    if choice == "y":
        save_dir = os.getcwd()  # idar hi save krty hain 
    else:
        location_dir = input("Enter the location/path where you want to save the files: ").strip()
        save_dir = os.path.join(location_dir, "stego_data")#creates a folder to store data at custom location
       # checks if the inputted directory exists or not 
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)  #creates the directory if the directory doesn't exist

    default_filename="encoded_image.png"
    # Save the image
    image_path = os.path.join(save_dir, default_filename)
    cv2.imwrite(image_path, image)
    
    # Save the key and ciphertext
    data_file_path = os.path.join(save_dir, "encryption_data.txt")
    with open(data_file_path, "w") as file:
        file.write(f"Secret Key: {secret_key}\n")
        file.write(f"Ciphertext: {ciphertext}")
    
    print(f"✅ Image saved at: {image_path}")
    print(f"✅ Encryption data saved at: {data_file_path}")

def Decrypt_stego_image(image, secret_key):
    bgr = 0  # channel=3 as by default cv2 reads in bgr format 0=blue,1=green,2=red
    height, width, channel = image.shape  # used to make sure rows and col don't go out of bounds by height for rows and width for col
    decrypted_message = ""
    cipher_text = input("Enter the cipher text for message pattern: ")
    tuple_list = decrypt_message(cipher_text, secret_key)
    # print("tuple list: ",tuple_list) # used to check if the cipher text for the row col patten is changed back to list of tuples
    
    rows = []
    cols = []
    for row, col in tuple_list:
        rows.append(row)
        cols.append(col)
        
    for i in range(len(rows)):
        decrypted_message = decrypted_message + num[image[rows[i], cols[i], bgr]]
        bgr = (bgr + 1) % 3
    print("Decrypted message: ", decrypted_message)

def unpad(text):
    """Removes padding after AES decryption."""
    return text[:-ord(text[-1])] if text else text

def decrypt_message(cipher_text, secret_key):
    """Decrypts an AES-encrypted message."""
    key = secret_key.ljust(16)[:16].encode("utf-8")  # Ensure 16-byte key
    decoded = base64.b64decode(cipher_text)
    iv = decoded[:16]
    encrypted_bytes = decoded[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    
    # Ensure we correctly unpad the message and decode it
    decrypted_text = unpad(decrypted_bytes.decode("utf-8"))
    
    tuples = convert_to_tuples(decrypted_text)  # decrypted text is the decrypted string of row,col that is converted to list of tuples
    # print("tuples: ",tuples) here it is just used to verify
    return tuples

def convert_to_tuples(decrypted_text):
    """Converts decrypted text into a list of tuples (row, col)."""
    # print("Decrypted text:", decrypted_text)  # Debugging line 
    numbers = list(map(int, decrypted_text.split()))
    result = []
    
    # Group every two numbers into a tuple (row, col)
    for i in range(0, len(numbers), 2):
        result.append((numbers[i], numbers[i+1]))
    #print(result) #debugging line used to check if string to tupple coversion is happening
    return result

if __name__ == "__main__":
    main()

