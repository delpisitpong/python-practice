from product import Product

def setting_product():
    names = ["GunCha", "KaTom", "KTaMin", "YaBaa"]
    prices = [200.1, 100.2, 400.3, 1500.4]
    quantities = [100, 100, 100, 3000000]
    
    products = []
    for i in range(len(names)):
        p = Product()
        p.name = names[i]
        p.price = prices[i]
        p.quantity = quantities[i]
        products.append(p)
    return products

def main():
    products = setting_product()

    print("welcome to NAAMBAI shop")
    print("=" * 50)
    print(f"Press [1] to buy GunCha (Stock = {products[0].quantity})")
    print(f"Press [2] to buy KaTom (Stock = {products[1].quantity})")
    print(f"Press [3] to buy KTaMin (Stock = {products[2].quantity})")
    print(f"Press [4] to buy YaBaa (Stock = {products[3].quantity})")
    print("=" * 50)

    choice = int(input("Enter a number: "))

    while True:
        if 1 <= choice <= 4:
            index = choice - 1
            selected_product = products[index]

            print("=" * 50)
            buy_amount = int(input(f"How many {selected_product.name} do you want to buy? "))

            if buy_amount <= selected_product.quantity:
                selected_product.sell(buy_amount)
                print("=" * 50)
                print(f"Total Price: {selected_product.price * buy_amount:.2f} Baht")
                print("=" * 50)
            else:
                print("\nNot enough item in stock ...\n\n")
                print("=" * 50)
                print(selected_product.show_info())
                print("=" * 50)

            break
        else:
            choice = int(input("Invalid number! Enter a number, again: "))

if __name__ == "__main__":
    main()