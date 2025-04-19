import csv
from typing import Dict

def read_products(filename: str) -> Dict[str, dict]:
    products = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products[row['sku']] = {
                'name': row['name'],
                'current_price': float(row['current_price']),
                'cost_price': float(row['cost_price']),
                'stock': int(row['stock'])
            }
    return products

def read_sales(filename: str) -> Dict[str, int]:
    sales = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales[row['sku']] = int(row['quantity_sold'])
    return sales

def calculate_new_price(product: dict, quantity_sold: int) -> float:
    new_price = product['current_price']
    
    if product['stock'] < 20 and quantity_sold > 30:
        new_price *= 1.15
    elif product['stock'] > 200 and quantity_sold == 0:
        new_price *= 0.7
    elif product['stock'] > 100 and quantity_sold < 20:
        new_price *= 0.9
    
    min_price = product['cost_price'] * 1.2
    if new_price < min_price:
        new_price = min_price
    
    new_price = round(new_price, 2)
    
    return new_price

def main():
    products = read_products('products.csv')
    sales = read_sales('sales.csv')
    
    output_data = []
    for sku, product in products.items():
        quantity_sold = sales.get(sku, 0)
        new_price = calculate_new_price(product, quantity_sold)
        
        output_data.append({
            'sku': sku,
            'old_price': f"{product['current_price']:.2f} USD",
            'new_price': f"{new_price:.2f} USD"
        })
    
    with open('updated_prices.csv', mode='w', newline='') as file:
        fieldnames = ['sku', 'old_price', 'new_price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(output_data)
    
    print("Updated prices written to updated_prices.csv")

if __name__ == '__main__':
    main()