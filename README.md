# 📞 Greek Bulk Phone Number Lookup Tool
## Description
This Python script performs automated bulk reverse Greek phone number lookups using data from 11888[.]gr. It can process a single number or multiple numbers from a file and save the results to an output file.
It is especially useful for cybercrime investigators who need to process multiple phone numbers efficiently, saving both time and effort by automating the lookup process!

## Features
✅ Lookup a single phone number.
✅ Lookup multiple numbers from a file.
✅ Save results to an output file.
✅ Handles encoding errors for non-UTF-8 files.

## ⚙️ Requirements

- Python 3.x
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

## 🚀 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/nkranidiotis/gr_phone_bulk_lookup.git
   cd gr_phone_bulk_lookup
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 📖 Usage

### 🔍 Single Number Lookup

```sh
python gr_phone_bulk_lookup.py 6970431540
```

### 📂 Multiple Numbers from File

```sh
python gr_phone_bulk_lookup.py --file numbers.txt
```

### 💾 Save Output to File

```sh
python gr_phone_bulk_lookup.py --file numbers.txt -o output.txt
```

## 📝 Example Output
```
Looking up: 6970431540
Phone: 6970431540
Name: GAKHAR R ACLAN
Address: Σάρδεων 8, 10446 - Περιφερεια Πρωτευουσης, Αττικη
```

If a number is not found:
```
Phone: 6992877026
Name: NULL
Address: NULL
```

## 📜 License
MIT License

## 👤 Author
Kranidiotis Nikolaos
https://osec.gr
