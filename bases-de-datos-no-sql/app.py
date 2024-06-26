import boto3

#Crear cliente para dynamodb
dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

tabla = dynamodb.Table('tabla-milena-zapata')

#Leer un elemento de la tabla
response = tabla.get_item(Key={'Id':'2'})
print(response['Item'])

#Leer todos los elementos de la tabla
response = tabla.scan()
print(response['Items'])

#Insertar elemento en la tabla
item = {
        'Id':'3',
        'Nombre':'Luis',
        'Ciudad':'Paris'
        }

tabla.put_item(Item=item)

response = tabla.scan()
print(response['Items'])

#Leer un elemento de la tabla
response = tabla.get_item(Key={'Id': '3'})

print("Elemento antes de actualizar", response['Item'])

response = tabla.update_item(
    Key={
        'Id': '3'  
    },
    UpdateExpression='SET Ciudad = :val1',  # Expresión de actualización
    ExpressionAttributeValues={
        ':val1': 'Milan'  # Nuevo valor para atributo
    }
)

#Leer un elemento de la tabla
response = tabla.get_item(Key={'Id': '3'})

print("Elemento despues de actualizar", response["Item"])