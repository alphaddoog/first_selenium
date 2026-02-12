from selenium import webdriver
from selenium.webdriver.common.by import By #IMPORTANDO METODO DE LOCALIZAÇÃO 
from selenium.webdriver.support.ui import WebDriverWait #ESPERA ACONTRCER ALGO PARA EXECUTAR OUTRO
from selenium.webdriver.support import expected_conditions as EC


navegador = webdriver.Chrome()#ABRIR O NAVEHADOR 
navegador.maximize_window()
navegador.get("https://www.google.com") #CARREGAR O URL 

wait = WebDriverWait(navegador, 10) #espera ate 15 segundos a pagina carregar

#ENCONTRAR CAMPO DE PESQUISA
campo = navegador.find_element(By.NAME, "q") #ARMAZENA A PROCURA DO ELEMNTO / priorizar id e NAME

campo.send_keys("Temperatura sobradinho") #ENVIANDO O TEXTO     

campo.submit() #BASICAMENTE CLICANDO - ENVIANDO A REQUISIÇÃO 

temperatura_elemento = wait.until(
    EC.presence_of_element_located((By.ID, "wob_tm"))
)

temperatura = temperatura_elemento.text

print(f"A temperatura em Sobradinho DF é: {temperatura}°C") 
navegador.quit()#ENCERRARA PAGÍNA 
 

