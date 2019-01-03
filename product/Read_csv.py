import csv
order={}
with open("import_sale_order_Final.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print({dict(row)['NAME']:{'address':dict(row)['ADDRESS'],'address 2':dict(row)['ADDRESS 2'],'zipcod':dict(row)['ZIPCODE'],'city':dict(row)['CITY'],'country':dict(row)['COUNTRY']}},
              {'reference':dict(row)['REFERENCE']},{'purchase_list':{'invoice to':dict(row)['INVOICE TO'],'customer id':dict(row)['CUSTOMER ID'],'SUPPLIER_REF_SKU':dict(row)['SUPPLIER_REF_SKU']}})
       
csvfile.close()
