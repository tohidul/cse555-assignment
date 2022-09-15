from flask import Flask, render_template, jsonify, request, redirect, url_for
import dbFunctions
# please edit the example_config.py file and edit the file name to config.py and connectionString variable
from config import connectionString

app = Flask(__name__)

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


@app.route('/product/editProduct/<productID>', methods=['GET', 'POST'])
def editProduct(productID):
    if(request.method=="GET"):
        productDict = db.getDataByProductID(productID)
        return render_template('editProduct.html', product=productDict)
    else:
        myQuery = {"productID": productID}
        newValues = {"$set": {}}
        newValues["$set"]["productID"] = request.form.get("productID", "")
        newValues["$set"]["productName"] = request.form.get("productName", "")
        newValues["$set"]["supplierName"] = request.form.get("supplierName", "")
        newValues["$set"]["productCategory"] = request.form.get("productCategory", "")
        newValues["$set"]["quantityPerUnit"] = request.form.get("quantityPerUnit", "")
        newValues["$set"]["unitPrice"] = request.form.get("unitPrice", "")
        newValues["$set"]["numberOfUnitAvailable"] = request.form.get("numberOfUnitAvailable", "")
        db.updateData(myQuery, newValues)
        return redirect("/")


@app.route('/product/deleteProductConfirmation/<productID>', methods=["GET"])
def deleteProductConfirmation(productID):
    if(request.method=="GET"):
        productDict = db.getDataByProductID(productID)
        return render_template("deleteProductConfirmation.html", product=productDict)
    else:
        return "GET Product ID"+request.form.get("shouldDelete")


@app.route('/product/delete/<productID>', methods=["GET", "POST"])
def deleteProduct(productID):
    if(request.method=="POST"):
        db.deleteByID(productID)
        return redirect("/")



@app.route('/product/createProduct', methods=['GET', 'POST'])
def createProduct():
    if (request.method == 'GET'):
        return render_template("createProduct.html", product=db.makeEmptyProductDict(), warningMessage="")
    else:
        dataDict = {}
        dataDict["productID"] = str(request.form.get("productID", ""))
        dataDict["productName"] = request.form.get("productName", "")
        dataDict["supplierName"] = request.form.get("supplierName", "")
        dataDict["productCategory"] = request.form.get("productCategory", "")
        dataDict["quantityPerUnit"] = request.form.get("quantityPerUnit", "")
        dataDict["unitPrice"] = request.form.get("unitPrice", "")
        dataDict["numberOfUnitAvailable"] = request.form.get("numberOfUnitAvailable", "")
        if(db.doesDocumentExistByID(dataDict["productID"])):
            # return redirect(url_for("createProduct", product=dataDict))
            return render_template("createProduct.html", product=dataDict, warningMessage="The product ID already Exists. Please change the product ID")
        else:
            db.insertData(dataDict)
            return redirect("/")


@app.route('/product/updateProduct/<productID>', methods=['GET', 'POST'])
def updateProduct(productID):
    if (request.method == 'GET'):
        return render_template("index.html")
    else:
        myQuery = {"productID": productID}
        newValues = {"$set": {}}
        newValues["$set"]["productID"] = request.form.get("productID", "")
        newValues["$set"]["productName"] = request.form.get("productName", "")
        newValues["$set"]["supplierName"] = request.form.get("supplierName", "")
        newValues["$set"]["productCategory"] = request.form.get("productCategory", "")
        newValues["$set"]["quantityPerUnit"] = request.form.get("quantityPerUnit", "")
        newValues["$set"]["unitPrice"] = request.form.get("unitPrice", "")
        newValues["$set"]["numberOfUnitAvailable"] = request.form.get("numberOfUnitAvailable", "")
        db.updateData(myQuery, newValues)



@app.route('/product/validateProduct')
def validateProduct():
    return jsonify({"productAlreadyExist": True})


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
