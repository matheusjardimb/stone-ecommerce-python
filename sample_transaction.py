# coding=utf-8

from uuid import UUID

from stoneEcommercePython.data_contracts.CreateSaleRequest import creditcard, creditcard_transaction, order, \
    create_sale_request
from stoneEcommercePython.enum_types.HttpContentTypeEnum import HttpContentTypeEnum
from stoneEcommercePython.enum_types.PlatformEnvironment import PlatformEnvironment
from stoneEcommercePython.stone_config.GatewayServiceClient import GatewayServiceClient

creditcard_data = creditcard(creditcard_number='4111111111111111',
                             creditcard_brand='Visa',
                             exp_month=10,
                             exp_year=2018,
                             security_code='123', holder_name='LUKE SKYWALKER')

# Cria a transação.
amount_in_cents = 10000
transaction_collection = [creditcard_transaction(amount_in_cents, creditcard_data)]

# Cria o numero do pedido
options_request = order(order_reference='NumeroDoPedido')

# Cria a request.
request = create_sale_request(creditcard_transaction_collection=transaction_collection, order=options_request)

merchant_key = UUID('00000000-0000-0000-0000-000000000000')
end_point = "https://transaction.stone.com.br"

environment = PlatformEnvironment.production
content_type = HttpContentTypeEnum.json
service_client = GatewayServiceClient(merchant_key, environment, content_type, end_point)

http_response = service_client.sale.create_with_request(request)

json_response = http_response.json()
print(json_response)
