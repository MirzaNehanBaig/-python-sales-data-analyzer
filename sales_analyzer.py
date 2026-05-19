# Mini Sales Data Analyzer

def analyze_sales():
    print("--- Sales Performance Report ---")
    
    # 1. Our dataset (a list of dollar amounts from today's sales)
    sales = [15.50, 120.00, 45.00, 300.00, 8.99, 95.50, 22.00]
    
    # 2. Set up our tracker variables
    total_revenue = 0
    highest_sale = 0
    
    # 3. Loop through every sale in our list
    for sale in sales:
        # Add the current sale to our total revenue
        total_revenue = total_revenue + sale
        
        # 4. Check if the current sale is the highest one so far
        if sale > highest_sale:
            highest_sale = sale  # Update the tracker box with the new record!

    # 5. Calculate the total number of sales and the average
    number_of_sales = len(sales)
    average_sale = total_revenue / number_of_sales

    # 6. Print the results (Using f-strings to format the data)
    print(f"Total Number of Sales: {number_of_sales}")
    print(f"Grand Total Revenue:   ${total_revenue:.2f}")
    print(f"Average Spend Per Customer: ${average_sale:.2f}")
    print(f"Highest Single Purchase:     ${highest_sale:.2f}")

# Call the function to run the data analysis
analyze_sales()