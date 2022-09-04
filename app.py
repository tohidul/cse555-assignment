from flask import Flask, render_template, jsonify, request, redirect
import dbFunctions
app = Flask(__name__)

connectionString = r"mongodb+srv://tohidul:tohidulcse555@cluster-cse555-assignme.tmjjjp8.mongodb.net/?retryWrites=true&w=majority"

db = dbFunctions.Product(connectionString, 'cse555-assignment', 'products')
# tempData = {
#     "productID": 1,
#     "productName": "computer"
# }
#
# test = db.insertData(tempData)
# db.getAllData()
# db.insertData(tempData)
# db.getAllData()


@app.route('/')
def showProducts():
    productList = db.getAllData()
    return render_template('index.html', products=productList)


@app.route('/product/edit/<productID>')
def editProduct(productID):
    productDict = db.getDataByProductID(productID)
    return render_template('editProduct.html', product = productDict)


@app.route('/product/delete/<productID>')
def deleteProduct(productID):
    return "productID"

@app.route('/product/createProduct', methods=['GET', 'POST'])
def createProduct():
    if(request.method=='GET'):
        return render_template("createProduct.html")
    else:
        dataDict = {}
        dataDict["productID"] = request.form.get("productID", "")
        dataDict["productName"] = request.form.get("productName", "")
        dataDict["supplierName"] = request.form.get("supplierName", "")
        dataDict["productCategory"] = request.form.get("productCategory", "")
        dataDict["quantityPerUnit"] = request.form.get("quantityPerUnit", "")
        dataDict["unitPrice"] = request.form.get("unitPrice", "")
        dataDict["numberOfUnitAvailable"] = request.form.get("numberOfUnitAvailable", "")
        db.insertData(dataDict)
        return redirect("/")


@app.route('/product/updateProduct/<productID>', methods=['GET', 'POST'])
def updateProduct(productID):
    if(request.method=='GET'):
        return render_template("index.html")
    else:
        myQuery = {"productID": productID}
        newValues= {"$set":{}}
        newValues["$set"]["productID"] = request.form.get("productID", "")
        newValues["$set"]["productName"] = request.form.get("productName", "")
        newValues["$set"]["supplierName"] = request.form.get("supplierName", "")
        newValues["$set"]["productCategory"] = request.form.get("productCategory", "")
        newValues["$set"]["quantityPerUnit"] = request.form.get("quantityPerUnit", "")
        newValues["$set"]["unitPrice"] = request.form.get("unitPrice", "")
        newValues["$set"]["numberOfUnitAvailable"] = request.form.get("numberOfUnitAvailable", "")
        db.updateData(myQuery,newValues)
        return redirect("/")

@app.route('/product/validateProduct')
def validateProduct():
    return jsonify({"productAlreadyExist": True})


if __name__ == '__main__':
    app.run()
