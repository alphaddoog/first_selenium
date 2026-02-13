"""
Projeto: Consulta automática de temperatura
Autor: Douglas
Descrição:
Este script abre o Google, pesquisa a temperatura de Sobradinho-DF
e exibe o resultado no terminal.
Usa Selenium para automatizar o navegador.
"""

# ==============================
# IMPORTAÇÕES
# ==============================
from selenium import webdriver  # Biblioteca principal para controlar o navegador
from selenium.webdriver.common.by import By  # Para localizar elementos (ID, NAME, etc.)
from selenium.webdriver.support.ui import WebDriverWait  # Para esperar elementos carregarem
from selenium.webdriver.support import expected_conditions as EC  # Condições de espera


# ==============================
# DEFINIÇÃO DE FUNÇÕES
# ==============================

def start_browser():
    """
    Inicializa o navegador Chrome e maximiza a janela.
    
    Retorna:
        webdriver.Chrome: instância do navegador
    """
    browser = webdriver.Chrome()  # Abrir o Chrome
    browser.maximize_window()  # Maximizar a janela
    return browser


def search_temperature(browser, city):
    """
    Pesquisa no Google a temperatura de uma cidade.
    
    Args:
        browser (webdriver.Chrome): instância do navegador
        city (str): nome da cidade para pesquisar
    
    Retorna:
        str: valor da temperatura como texto
    """
    wait = WebDriverWait(browser, 15)  # Espera até 15 segundos pelos elementos

    # Abrir Google
    browser.get("https://www.google.com")

    # Esperar o campo de pesquisa aparecer
    search_field = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))  # Localiza campo pelo NAME
    )

    # Digitar pesquisa
    search_field.send_keys(f"temperature {city}")

    # Enviar pesquisa (como apertar ENTER)
    search_field.submit()

    # Esperar widget de temperatura aparecer
    temperature_element = wait.until(
        EC.presence_of_element_located((By.ID, "wob_tm"))  # ID do widget do Google
    )

    # Retornar valor da temperatura
    return temperature_element.text


def display_temperature(city, temperature):
    """
    Exibe a temperatura de forma formatada no console.
    
    Args:
        city (str): nome da cidade
        temperature (str): valor da temperatura
    """
    print("=" * 40)
    print("TEMPERATURE CHECK")
    print("=" * 40)
    print(f"City: {city}")
    print(f"Current temperature: {temperature}°C")
    print("=" * 40)


def main():
    """
    Função principal:
    - Inicializa o navegador
    - Pesquisa a temperatura
    - Exibe o resultado
    - Fecha o navegador
    """
    city = "Sobradinho DF"  # Cidade a ser pesquisada

    browser = start_browser()  # Abrir navegador

    try:
        # Buscar temperatura
        temperature = search_temperature(browser, city)
        # Exibir resultado
        display_temperature(city, temperature)

    except Exception as error:
        # Tratar erros inesperados
        print("Ocorreu um erro durante a execução:", error)

    finally:
        # Sempre fechar o navegador
        browser.quit()


# ==============================
# EXECUÇÃO
# ==============================
if __name__ == "__main__":
    main()
