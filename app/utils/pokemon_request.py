import requests

def get_pokemons():
    url = f"https://pokeapi.co/api/v2/pokemon/10248/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados da API: {e}")
        return None
    
def obter_dados_pokemon(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção para erros HTTP

        data = response.json()
        species_name = data['species']['name']  # Extrai o nome do species

        # Verifica se 'other' existe e, em seguida, acessa 'official-artwork' dentro dele
        if 'other' in data['sprites']:
            other = data['sprites']['other']
            if 'official-artwork' in other:
                official_artwork_url = other['official-artwork']['front_default']
            else:
                official_artwork_url = None

            # Verifica se 'showdown' existe e, em seguida, acessa 'front_default' dentro dele
            if 'showdown' in other:
                showdown_url = other['showdown']['front_default']
            else:
                showdown_url = None
        else:
            official_artwork_url = None
            showdown_url = None

        return species_name, official_artwork_url, showdown_url
    except requests.exceptions.RequestException as e:
        # Trata erros de solicitação, como conexão perdida, URL inválida, etc.
        print(f"Erro ao buscar dados da API: {e}")
        return None, None, None
    
def obter_urls_pokemons(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção para erros HTTP

        data = response.json()
        pokemons = [(pokemon['name'], pokemon['url']) for pokemon in data['results']]

        dados_pokemons_lista = []

        # Para cada tupla (nome, url) na lista de pokemons, chama a função obter_dados_pokemon
        for nome, url in pokemons:
            dados_pokemon = obter_dados_pokemon(url)
            dados_pokemons_lista.append(dados_pokemon)
        return dados_pokemons_lista
    except requests.exceptions.RequestException as e:
        # Trata erros de solicitação, como conexão perdida, URL inválida, etc.
        print(f"Erro ao buscar dados da API: {e}")
        return None