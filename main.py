import requests
from datetime import date

data_hoje = date.today().strftime("%m-%d-%Y")
url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_hoje}'&$top=31&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Status Code Error: {response.status_code}")

dol_valor_compra =data['value'][0]['cotacaoCompra']
dol_valor_venda = data['value'][0]['cotacaoVenda']
dol_data = data['value'][0]['dataHoraCotacao']

print(f'Data: {dol_data},\nCompra: {dol_valor_compra},\nVenda: {dol_valor_venda}')
print('=====================================================================')