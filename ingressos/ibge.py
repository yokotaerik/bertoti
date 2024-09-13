import requests

class Ibge:
    def obter_cidades_por_estado(self, estado_id):
        url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado_id}/municipios"
        response = requests.get(url)
        
        if response.status_code == 200:
            cidades = response.json()
            return [cidade['nome'] for cidade in cidades]
        else:
            return []

    estados = {
        "Acre": 12, "Alagoas": 27, "Amapá": 16, "Amazonas": 13, "Bahia": 29, "Ceará": 23,
        "Distrito Federal": 53, "Espírito Santo": 32, "Goiás": 52, "Maranhão": 21,
        "Mato Grosso": 51, "Mato Grosso do Sul": 50, "Minas Gerais": 31, "Pará": 15,
        "Paraíba": 25, "Paraná": 41, "Pernambuco": 26, "Piauí": 22, "Rio de Janeiro": 33,
        "Rio Grande do Norte": 24, "Rio Grande do Sul": 43, "Rondônia": 11, "Roraima": 14,
        "Santa Catarina": 42, "São Paulo": 35, "Sergipe": 28, "Tocantins": 17
    }
    


print(Ibge.obter_cidades_por_estado(Ibge,35))