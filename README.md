# 🔐 Image Encryption Tool (Pixel Manipulation)

- 📁 Upload an image and encrypt/decrypt instantly using CLI  
- 🔁 Fully reversible encryption using the same key  
- 🧩 Supports multiple pixel manipulation techniques  

---

## 🛠 Tech Stack

- **Language:** Python 3  
- **Image Processing:** Pillow (PIL)  
- **Numerical Operations:** NumPy  
- **Interface:** Command Line (argparse)  

---

## 🚀 Features

- 🔢 XOR-based pixel value encryption  
- 🔀 Pixel swapping (position-based encryption)  
- 🔑 Key-based reversible encryption  
- 📸 Makes images visually unreadable (Swap Mode)  
- 🧪 Educational & easy-to-understand implementation  

---


```bash
#installation
pip install pillow numpy

🧪 Usage

# XOR Encryption Command
#Encrypt
python image_crypto.py --mode xor --input input.png --output xor_encrypted.png --key 123
#Decrypt
python image_crypto.py --mode xor --input xor_encrypted.png --output xor_decrypted.png --key 123

#Swap Mode
#Encrypt
python image_crypto.py --mode swap --input input.png --output swap_encrypted.png --key 123
#Decrypt
python image_crypto.py --mode swap --input swap_encrypted.png --output swap_decrypted.png --key 123
```

Note: rename the file to input.png

