# SCT_SD_4

🛍️ E-commerce Product Scraper using Python GUI
This project is a Python-based GUI application that allows users to scrape product data such as name, price, and rating from an e-commerce website and save the data into a CSV file. The interface is built using Tkinter, and web scraping is performed using the BeautifulSoup and requests libraries.

It is ideal for beginners learning GUI development, web scraping, and file handling in Python.

✅ Features
🖥️ Simple and intuitive Tkinter-based GUI

🌐 Input any supported e-commerce URL

📦 Extracts product Name, Price, and Rating

📁 Exports data to a clean, structured products.csv file

💡 Built-in error handling and success messages

🧪 Sample Supported URL
Use this link for testing (BooksToScrape):

bash
Copy
Edit
https://books.toscrape.com/catalogue/category/books_1/page-1.html

🔧 Technologies Used
Python 3.x

Tkinter (GUI)

requests (HTTP requests)

BeautifulSoup (HTML parsing)

csv (Data export)

🚀 How to Run
Clone or download this repository.

Install required libraries:

bash
Copy
Edit
pip install requests beautifulsoup4
Run the script:

bash
Copy
Edit
python scraper_gui.py
Enter a product listing URL and click “Scrape and Save”.

📂 Output
A file named products.csv will be created with data like:

python-repl
Copy
Edit
Name, Price, Rating
The Shell Seekers, £52.15, Four
A Light in the Attic, £51.77, Three
...
