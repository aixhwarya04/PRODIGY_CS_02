from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img, dtype=np.uint8)
    
    # Prevent overflow
    encrypted_array = (img_array.astype(np.int16) + key) % 256
    encrypted_array = encrypted_array.astype(np.uint8)
    
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img, dtype=np.uint8)
    
    # Prevent overflow
    decrypted_array = (img_array.astype(np.int16) - key) % 256
    decrypted_array = decrypted_array.astype(np.uint8)
    
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    print("=== Image Encryption Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    input_path = input("Enter input image path: ").strip()
    output_path = input("Enter output image path: ").strip()
    key = int(input("Enter encryption/decryption key (integer 1-255): "))

    if choice == 'e':
        encrypt_image(input_path, output_path, key)
    elif choice == 'd':
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice! Please enter 'E' or 'D'.")
