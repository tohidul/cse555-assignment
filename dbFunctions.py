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
            productDict = {}
            productDict["productID"] = getattr(product, "productID", "")
            productDict["productName"] = getattr(product, "productName", "")
            productDict["supplierName"] = getattr(product, "supplierName", "")
            productDict["productCategory"] = getattr(product, "productCategory", "")
            productDict["quantityPerUnit"] = getattr(product, "quantityPerUnit", "")
            productDict["unitPrice"] = getattr(product, "unitPrice", "")
            productDict["numberOfUnitAvailable"] = getattr(product, "numberOfUnitAvailable", "")
            dataList.append(productDict)

        return dataList

    def insertData(self, dataDictionary):
        return self.productCollection.insert_one(dataDictionary).inserted_id



