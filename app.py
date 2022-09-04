from flask import Flask, render_template, jsonify, request
import dbFunctions
app = Flask(__name__)

connectionString = r"mongodb+srv://tohidul:tohidulcse555@cluster-cse555-assignme.tmjjjp8.mongodb.net/?retryWrites=true&w=majority"

db = dbFunctions.Product(connectionString, 'cse555-assignment', 'products')
tempData = {
    "productID": 1,
    "productName": "computer"
}

test = db.insertData(tempData)
db.getAllData()
# db.insertData(tempData)
# db.getAllData()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/product')
def showProducts():
    sampleProducts = [
        {"productID": 1,
         "productName": 'test product',
         "supplierName": "adsd",
         "productCategory": 'adsd',
         "quantityPerUnit": "as",
         "unitPrice": 23,
         "numberOfUnitAvailable": 4,
         "action": "action"},
        {"productID": 2,
         "productName": 'test product2',
         "supplierName": "adsd2",
         "productCategory": 'adsd',
         "quantityPerUnit": "as",
         "unitPrice": 23,
         "numberOfUnitAvailable": 4,
         "action": "action"}
    ]
    return render_template('index.html', products=sampleProducts)


@app.route('/product/edit/<int:productID>')
def editProduct(productID):
    return "productID"


@app.route('/product/delete/<int:productID>')
def deleteProduct(productID):
    return "productID"

@app.route('/product/createProduct', methods=['GET', 'POST'])
def createProduct():
    if(request.method=='GET'):
        return render_template("createProduct.html")
    else:
        return jsonify(request.form)


@app.route('/product/updateProduct', methods=['GET', 'POST'])
def updateProduct():
    if(request.method=='GET'):
        return render_template("index.html")
    else:
        return jsonify(request.form)


@app.route('/product/validateProduct')
def validateProduct():
    return jsonify({"productAlreadyExist": True})


if __name__ == '__main__':
    app.run()
