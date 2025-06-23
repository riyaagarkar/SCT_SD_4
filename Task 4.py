import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape data
def scrape_data():
    url = entry_url.get()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        products = soup.find_all("article", class_="product_pod")

        if not products:
            messagebox.showinfo("Info", "No products found. Check the URL.")
            return

        data = []
        for product in products:
            name = product.h3.a["title"]
            price = product.find("p", class_="price_color").text.strip()
            rating = product.p.get("class")[1] if len(product.p.get("class")) > 1 else "Not rated"
            data.append([name, price, rating])

        with open("products.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Price", "Rating"])
            writer.writerows(data)

        messagebox.showinfo("Success", "Data saved to products.csv")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Window
root = tk.Tk()
root.title("E-commerce Product Scraper")

tk.Label(root, text="Enter URL of e-commerce page:").pack(pady=10)
entry_url = tk.Entry(root, width=50)
entry_url.pack()

ttk.Button(root, text="Scrape and Save", command=scrape_data).pack(pady=20)

root.mainloop()
