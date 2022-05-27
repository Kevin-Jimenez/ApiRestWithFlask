from flask import Flask, jsonify, request 

app = Flask(__name__) #inicializamos

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"productos":products})
#Returns All products

@app.route('/products/<string:name_id>')
def getProduct(name_id):
    productFound = [product for product in products if product['name'] == name_id]
    if(len(productFound) > 0):
        print(name_id)
        return jsonify({"Producto":productFound[0]})
    else:
        return jsonify({"message":"Product not found"})
#Return product 

@app.route('/products', methods=['POST'])
def agregarProducto():
    newproduct = {
        "name": request.json['name'], 
        "price": request.json['price'],
        "quantity" : request.json['quantity'] 
    }
    products.append(newproduct)
    return jsonify({
        "message":"Producto agregado satisfactoriamente", 
        "Products":products
        })
#It't an insert 

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message":"Producto Actualizado",
            "Producto": productFound[0]
        })
    return jsonify({
        "message": "Product not found"
    })
#Update product

@app.route('/products/<string:product_name>', methods=['DELETE'])
def eliminarProducto(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({
            "message":"Producto Eliminado",
            "productos": products
        })
    return jsonify({
        "message":"Producto no encontrado"
    })
#Delete Product

#init app
if __name__ == '__main__':
    app.run(debug=True,port=5000)
