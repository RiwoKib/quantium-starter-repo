import csv, os 
        

with open('pink_morsel_sales.csv', 'w') as pink_sales:
    header_row = ['Sales', 'Date' ,'Region']
    writer = csv.DictWriter(pink_sales, fieldnames=header_row)

    writer.writeheader()

    #loop through the data folder
    for filename in os.listdir('data'):
        #select csv files
        if filename.endswith('.csv'):
            #open and read the files
            with open('data/'+filename, 'r') as sales_data:
                reader = csv.DictReader(sales_data)

                #read each row containing pink morsel and collect sales, date and region

                for row in reader:
                    if row['product'] == 'pink morsel': 
                        price = row['price']
                        total_sales = float(price[1:]) * int(row['quantity'])
                        date_sold = row['date']
                        region = row['region']

                        writer.writerow({'Sales':total_sales,
                                         'Date': date_sold,
                                         'Region': region})
                        
                        #print(f'{total_sales}\t{date_sold}\t{region}')
            
