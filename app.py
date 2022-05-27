from flask import Flask, jsonify, request #Importar librerias

app = Flask(__name__) #inicializamos
#importamos el archivo products que almacena los productos, simula la base de datos
from products import products 
#primera funcion solo para probar que funciona retorna Pong
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message":"Pong"})
#fin prueba


#Funcion nos retorna todos los productos --SIMILAR A UN SELECT
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"productos":products})
#FIN


#Funcion retorna el producto que seleccionemos --SIMILAR A UN SELECT WHERE pasandolo como parametro
@app.route('/products/<string:name_id>')
def getProduct(name_id):#le pasamos el nombre como parametro
    #Siguiente linea primero recorre los productos y busca el que le pasemos en la url name_id
    productFound = [product for product in products if product['name'] == name_id]
    if(len(productFound) > 0):
        print(name_id)
        return jsonify({"Producto":productFound[0]})#retornamos el primer producto encontrado, que coinsida
    else:
        return jsonify({"message":"Product not found"})#Sino encuentra el prodcuto retorna el mensaje
#FIN


#Funcion para hacer un insert con el metodo post capturamos los dartos insetados con el request
@app.route('/products', methods=['POST'])
def agregarProducto():
    newproduct = {
        "name": request.json['name'], #almacena el name del request
        "price": request.json['price'], #almacena el price del request
        "quantity" : request.json['quantity'] #almacena el quantity del request
    }
    products.append(newproduct)#se agrega a la lista de productos
    return jsonify({
        "message":"Producto agregado satisfactoriamente", 
        "Products":products
        })
#FIN


#Funcion actualizar metodfo PUT recojemos los datos del producto con el product_name como parametro
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):#Si encontro el producto entonces actualicelo y coja los valores de lso request
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
#FIN


#Funcion eliminar busca el nombre del producto, el cual pasamos por parametro y lo remueve de la lista    
@app.route('/products/<string:product_name>', methods=['DELETE'])
def eliminarProducto(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        products.remove(productFound[0])#le indicamos que elimine el producto encontrado en la posicion 0 que nos indica fue el primero
        return jsonify({
            "message":"Producto Eliminado",
            "productos": products
        })
    return jsonify({
        "message":"Producto no encontrado"
    })
#FIN

#inicia la app
if __name__ == '__main__':
    app.run(debug=True,port=5000)
