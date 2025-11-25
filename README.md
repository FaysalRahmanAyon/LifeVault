<img width="990" height="665" alt="image" src="https://github.com/user-attachments/assets/ebafa764-c6b4-478d-86c8-6722968eac8e" />

# **LifeVault: Secure Digital Inheritance System**

**LifeVault** is a "dead man's switch" solution for your digital life. It allows you to aggregate critical digital assets (bank accounts, crypto wallets, legal documents), encrypt them client-side into a portable .vault file, and provide a secure, offline Python mechanism for your beneficiaries to recover them.

## **🛑 The Problem**

We live in a world of scattered digital fragility. If you were incapacitated today.

* Your family would not know your crypto seed phrases.  
* They would be locked out of your email (2FA).  
* They wouldn't know which recurring subscriptions to cancel.

Existing solutions rely on third-party servers (trust issues) or simple sticky notes (security risk).

## **🛡️ Architecture & Security**

LifeVault operates on a **Zero-Knowledge** and **Local-Only** architecture.

1. **Frontend:** A single-file HTML.  
   * **Encryption:** Uses the browser's native Web Crypto API.  
   * **Algorithm:** AES-GCM (Galois/Counter Mode) with a 256-bit key.  
   * **Data Flow:** Data is encrypted in your RAM. No data is ever sent to a server.  
2. **Backend (The Key):** A standalone Python script.  
   * **Decryption:** Uses the standard cryptography library to unlock .vault files.  
   * **Offline:** Designed to run without internet access for maximum security.

**⚠️ WARNING:** There is no "Forgot Password" feature. If you lose the Master Key, the .vault file is mathematically impossible to open.

## **🚀 Getting Started**

### **Prerequisites**

* A modern web browser (Chrome, Firefox, Edge).  
* Python 3.x installed (for the recovery script).

### **Installation**

1. Clone this repository:  
```java
git clone https://github.com/FaysalRahmanAyon/LifeVault.git  
cd lifevault
```
3. Install Python dependencies:  
```java
pip install \-r requirements.txt
```
## **📖 Usage Guide**

### **Phase 1: Creating the Vault (The User)**

1. Open index.html in your web browser.  
2. Select a category (Financial, Crypto, Legal, etc.).  
3. Fill in the details for your asset.  
   * *Note: Context-aware fields will adjust based on the category selected.*  
4. Repeat for all critical assets.  
5. Click **Lock & Export**.  
6. **CRITICAL:** Copy the **Master Key** displayed on the screen. This is the ONLY time it will be shown.  
7. Download the .vault file.

### **Phase 2: The Storage Protocol (Best Practice)**

To ensure security, separate the **Lock** (the file) from the **Key**:

* **The File:** Store the .vault file on a cloud drive (Google Drive/Dropbox), email it to your spouse, and keep a copy on a USB drive.  
* **The Key:** Write the Master Key on paper. Store it in a physical safe, or give it to your lawyer/trustee.

### **Phase 3: Recovering the Data (The Beneficiary)**

When the time comes to access the data:

1. Locate the .vault file and the Master Key.  
2. Place the .vault file in the same folder as vault\_opener.py.  
3. Run the recovery script:python vault\_opener.py
4. Enter the filename and the Master Key when prompted.  
5. The script will decrypt the data and display it in the terminal.

## **📦 File Structure**
```java
lifevault/  
├── index.html         
├── vault\_opener.py    
├── requirements.txt    
└── README.md          
```
## **⚖️ Disclaimer**

This software is provided "as is", without warranty of any kind. The authors are not responsible for any data loss caused by lost keys or improper usage. This tool is a utility for organization and encryption; it is not a legal substitute for a Last Will and Testament.

## **🤝 Contributing**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## **📄 License**

[MIT](https://choosealicense.com/licenses/mit/)
