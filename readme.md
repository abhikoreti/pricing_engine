# Pricing Engine - Readme

## Overview

This Python script automatically adjusts product prices based on inventory levels and recent sales performance. It applies predefined pricing rules to optimize revenue while ensuring a minimum profit margin.

**Features**

-   Reads product and sales data from CSV files.

-   Applies dynamic pricing rules based on stock levels and sales.

-   Ensures prices maintain a minimum 20% profit margin.

-   Generates an updated price list in CSV format.

## File Structure

```
pricing_engine/
│── products.csv          # Input: Product catalog (SKU, price, cost, stock)
│── sales.csv             # Input: Recent sales data (SKU, quantity sold)
│── pricing_engine.py     # Main Python script
│── updated_prices.csv    # Output: New prices after adjustment
```

## Pricing Rules

The script applies rules in priority order:

1. **Rule 1: Low Stock, High Demand**

    - Condition: `stock < 20` and `quantity_sold > 30`

    - Action: Increase price by 15%

2. **Rule 2: Dead Stock**

    - Condition: `stock > 200` and `quantity_sold == 0`

    - Action: Decrease price by 30%

3. **Rule 3: Overstocked Inventory**

    - Condition: `stock > 100` and `quantity_sold < 20`

    - Action: Decrease price by 10%

4. **Rule 4: Minimum Profit Constraint** (_Always Applied Last_)

    - Condition: New price must be **≥ 20% above cost price**.

    - Action: If below threshold, set to `cost_price * 1.2`.

5. **Final Rounding**

    - Prices are rounded to 2 decimal places.

## Output File (updated_prices.csv)

After execution, the script generates:

-   `sku` (Product ID)

-   `old_price` (Previous price)

-   `new_price` (Adjusted price)

## How To Run

1. **Prerequisites**

-   Python 3.6+ installed

-   VS Code (or any Python IDE)

2. **Steps**

    1. Place input files (`products.csv`, `sales.csv`) in the same folder as the script.

    2. Run the script in terminal:

        ```
        python pricing_engine.py
        ```

    3. Check output:

        - The script generates `updated_prices.csv`.

        - Logs confirmation:
            ```
            Updated prices written to updated_prices.csv
            ```

## Assumptions

-   Only the **first applicable rule (1-3)** is applied before enforcing Rule 4.

-   If a product’s `sku` is missing in `sales.csv`, it assumes `quantity_sold = 0`.

-   Prices are displayed with **USD units** in the output.
