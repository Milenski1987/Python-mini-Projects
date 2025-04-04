from helpers import clean_screen
import tkinter as tk
import json
from  canvas import app
from PIL import Image, ImageTk
import os


base_dir = os.path.dirname(__name__)


def update_current_user(username, p_id):
    with open("data/users.txt", "r+", newline="\n") as file:
        users = [json.loads(user.strip()) for user in file]
        for user in users:
            if user['username'] == username:
                user['products'].append(p_id)
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(user) + "\n" for user in users])
                return


def update_products(p_id):
    with open("data/products.txt", "r+") as file:
        products = [json.loads(product.strip()) for product in file]
        for product in products:
            if p_id == product['id']:
                product['count'] -= 1
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(product) + "\n" for product in products])
                return


def buy_product(product):
    clean_screen()

    with open("data/current_user.txt") as file:
        username = file.read()

    if username:
        update_current_user(username, product)
        update_products(product)

    render_products_screen()


def render_products_screen():
    clean_screen()

    with open("data/products.txt") as file:
        products = [json.loads(product.strip("\n")) for product in file]
        products = [product for product in products if product['count'] > 0]
        products_per_line = 6
        rows_per_product = len(products[0])
        for i, product in enumerate(products):
            row = i // products_per_line * rows_per_product
            column = i % products_per_line

            tk.Label(app, text=product["name"]).grid(row=row, column=column)

            img = Image.open(os.path.join(base_dir, "data/images", product["img_path"])).resize((100,100))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(image=photo_image)
            image_label.image = photo_image
            image_label.grid(row=row + 1, column=column)


            tk.Label(app, text=product['count']).grid(row=row+2, column=column)

            tk.Button(app,
                      text=f"Buy {product['id']}",
                      command=lambda p = product['id']: buy_product(p)
                      ).grid(row= row + 3, column= column)

