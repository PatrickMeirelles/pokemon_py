from utils import pokemon_request
import streamlit as st

response = pokemon_request.obter_urls_pokemons('https://pokeapi.co/api/v2/pokemon?limit=10&offset=0')


def obter_urls_imagens_oficiais(dados_pokemons):
    urls_imagens_oficiais = []

    for pokemon in dados_pokemons:
        urls_imagens_oficiais.append(pokemon[1])  # Adiciona a URL da imagem oficial de cada Pokémon

    return urls_imagens_oficiais

for nome, url_imagem_oficial, url_imagem_showdown in response:
    st.write(f"Nome do Pokemon: {nome}")
    st.image(url_imagem_oficial, output_format='JPEG')

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)