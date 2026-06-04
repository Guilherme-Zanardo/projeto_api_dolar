# BIBLIOTECAS
import requests
from datetime import date

# VERIFICAÇÃO DE DATAS
data_hoje = date.today().strftime("%m-%d-%Y")

# EXECUTA API
try:
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_hoje}'&$top=31&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Status Code Error: {response.status_code}")

    dol_valor_compra =data['value'][0]['cotacaoCompra']
    dol_valor_venda = data['value'][0]['cotacaoVenda']
    dol_data = data['value'][0]['dataHoraCotacao']

    print(f'\n=====================================================================')
    print(f'Data: {dol_data},\nCompra: {dol_valor_compra},\nVenda: {dol_valor_venda}')
    print(f'=====================================================================\n')

except Exception as e:
    if date.today().weekday() not in [5, 6]:  # Verifica se é fim de semana
        print(f'\n=====================================================================')
        print("Hoje é um dia não útil. O valor do dólar não será atualizado.")
        print(f'=====================================================================\n')
    else:
        print(f'\n=====================================================================')
        print(f"Erro ao acessar a API: {e}")
        print(f'=====================================================================\n')