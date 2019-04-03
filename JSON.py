import json



warehouse = '''[{"status":true,"message":"data saved successfully","data1":{"command":"SELECT","rowCount":3,"oid":null,"rows":[{"item_name":"embrator strawberry  juice","item_code":"0015","barcode":"2003403560278    ","type_name":".200ml","customer_qty":2,"cost":"1.180","customer_price":"0.590"},{"item_name":"embrator mango  juice","item_code":"0016","barcode":"2003403560285    ","type_name":".200ml","customer_qty":2,"cost":"1.180","customer_price":"0.590"},{"item_name":"embrator mango  juice","item_code":"0016","barcode":"2003403560285    ","type_name":".200ml","customer_qty":2,"cost":"1.180","customer_price":"0.590"}],"fields":[{"name":"item_name","tableID":16472,"columnID":2,"dataTypeID":1043,"dataTypeSize":-1,"dataTypeModifier":79,"format":"text"},{"name":"item_code","tableID":16472,"columnID":14,"dataTypeID":1043,"dataTypeSize":-1,"dataTypeModifier":14,"format":"text"},{"name":"barcode","tableID":16472,"columnID":12,"dataTypeID":1043,"dataTypeSize":-1,"dataTypeModifier":34,"format":"text"},{"name":"type_name","tableID":16464,"columnID":2,"dataTypeID":1043,"dataTypeSize":-1,"dataTypeModifier":34,"format":"text"},{"name":"customer_qty","tableID":16445,"columnID":4,"dataTypeID":23,"dataTypeSize":4,"dataTypeModifier":-1,"format":"text"},{"name":"cost","tableID":16445,"columnID":5,"dataTypeID":1700,"dataTypeSize":-1,"dataTypeModifier":-1,"format":"text"},{"name":"customer_price","tableID":16445,"columnID":3,"dataTypeID":1700,"dataTypeSize":-1,"dataTypeModifier":-1,"format":"text"}],"_parsers":[null,null,null,null,null,null,null],"RowCtor":null,"rowAsArray":false},"data2":{"command":"SELECT","rowCount":1,"oid":null,"rows":[{"invoice_date":"2019-02-07T08:06:21.355Z","total_amount":"2.360","invoice_no":"000464","user_name":"Test","customer_name":"Test-1111"}],"fields":[{"name":"invoice_date","tableID":16686,"columnID":6,"dataTypeID":1184,"dataTypeSize":8,"dataTypeModifier":-1,"format":"text"},{"name":"total_amount","tableID":16686,"columnID":5,"dataTypeID":1700,"dataTypeSize":-1,"dataTypeModifier":-1,"format":"text"},{"name":"invoice_no","tableID":16686,"columnID":2,"dataTypeID":1043,"dataTypeSize":-1,"dataTypeModifier":34,"format":"text"},{"name":"user_name","tableID":16386,"columnID":2,"dataTypeID":1043,"dataTypeSize":-1,"dataTypeModifier":34,"format":"text"},{"name":"customer_name","tableID":0,"columnID":0,"dataTypeID":25,"dataTypeSize":-1,"dataTypeModifier":-1,"format":"text"}],"_parsers":[null,null,null,null,null],"RowCtor":null,"rowAsArray":false}}]'''

data = json.loads(warehouse)

val = data[0]
data_1 = val['data1']
rows = data_1['rows']
dic_value = rows[0]
cost = dic_value["cost"]
print(cost)

print("--------------")

counter = 0
for i in rows:
    if counter <= len(rows):
        dic1 = rows[counter]
        type(dic1)
        counter += 1
print(dic1)
jsonstring = json.dumps(rows, indent=2, sort_keys=True)
# print(jsonstring)

rows = data_1['rows']
new_item_name = [d['item_name'] for d in rows]
if len(new_item_name) != len(set(new_item_name)):
    print("False")
else:
    print("True")
