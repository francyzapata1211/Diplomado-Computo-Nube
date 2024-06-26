import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')  

#Eliminar la tabla
response = dynamodb.delete_table(
    TableName='tabla-milena-zapata-2'
)

# Crear la tabla
# response = dynamodb.create_table(
#     TableName='tabla-milena-zapata-2',
#     KeySchema=[
#         {
#             'AttributeName': 'Id',
#             'KeyType': 'HASH'  
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'Id',
#             'AttributeType': 'S'  
#         }
#     ],
#     BillingMode='PAY_PER_REQUEST'  # Configurar capacidad bajo demanda
# )