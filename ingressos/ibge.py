import requests

def get_estados_cidades():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
    response = requests.get(url)
    
    if response.status_code == 200:
        municipios = response.json()
        estados_cidades = {}

        for municipio in municipios:
            cidade = municipio['nome']
            estado = municipio['microrregiao']['mesorregiao']['UF']['nome']
            
            # Verifica se o estado já existe no dicionário, se não, cria a chave
            if estado not in estados_cidades:
                estados_cidades[estado] = []
            
            # Adiciona a cidade à lista correspondente ao estado
            estados_cidades[estado].append(cidade)
        
        return estados_cidades
    else:
        raise Exception(f"Erro ao acessar a API do IBGE: {response.status_code}")
