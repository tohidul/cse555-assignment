import pymongo


class Product:
    def __init__(self, connectionString, dbName, collectionName):
        self.client = pymongo.MongoClient(connectionString, serverSelectionTimeoutMS=5000)
        self.db = self.client[dbName]
        self.productCollection = self.db[collectionName]

    def getDB(self):
        return self.db

    def getCollection(self):
        return self.productCollection

    def getAllData(self):
        dataList = []
        for product in self.productCollection.find():
            dataList.append(product)

        return dataList

    def getDataByProductID(self, productID):
        product = self.productCollection.find_one({"productID": productID})
        return product

    def insertData(self, dataDictionary):
        return self.productCollection.insert_one(dataDictionary).inserted_id

    def updateData(self, myQuery, newValues):
        self.productCollection.update_one(myQuery, newValues)

    def makeProductDict(self, mongoProductObj):
        productDict = {}
        productDict["productID"] = getattr(mongoProductObj, "productID", "")
        productDict["productName"] = getattr(mongoProductObj, "productName", "")
        productDict["supplierName"] = getattr(mongoProductObj, "supplierName", "")
        productDict["productCategory"] = getattr(mongoProductObj, "productCategory", "")
        productDict["quantityPerUnit"] = getattr(mongoProductObj, "quantityPerUnit", "")
        productDict["unitPrice"] = getattr(mongoProductObj, "unitPrice", "")
        productDict["numberOfUnitAvailable"] = getattr(mongoProductObj, "numberOfUnitAvailable", "")
        return productDict


    def makeEmptyProductDict(self):
        productDict = {}
        productDict["productID"] = ""
        productDict["productName"] = ""
        productDict["supplierName"] = ""
        productDict["productCategory"] = ""
        productDict["quantityPerUnit"] = ""
        productDict["unitPrice"] = ""
        productDict["numberOfUnitAvailable"] = ""
        return productDict

    def doesDocumentExistByID(self, productID):
        if (self.productCollection.count_documents({'productID': productID}, limit=1)) != 0:
            return True
        return False
