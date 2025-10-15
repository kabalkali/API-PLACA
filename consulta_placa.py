import sys # Importar a biblioteca sys para ler argumentos
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# ... (o resto das suas importações e a função processar_e_imprimir_tabela continuam iguais) ...

def main():
    # Pega a placa do primeiro argumento da linha de comando
    if len(sys.argv) < 2:
        print("ERRO: Forneça uma placa como argumento.")
        print("Exemplo: python consulta_placa.py ABC1234")
        return # Encerra se nenhuma placa foi passada

    placa_para_consultar = sys.argv[1]

    # --- CONFIGURAÇÃO DO DRIVER ---
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu') # Boa prática para headless
    options.add_argument("window-size=1024,768") # Evita problemas de layout
    driver = webdriver.Chrome(options=options)
    print("Navegador virtual (Chrome) iniciado.")

    # --- LÓGICA DE CONSULTA (simplificada para uma única execução) ---
    url_template = "https://placafipe.com/placa/{placa}" # Usando apenas uma URL como exemplo
    placa_formatada_url = placa_para_consultar.lower().replace('-', '')
    url_direta = url_template.format(placa=placa_formatada_url)

    print(f"\nIniciando consulta para a placa: {placa_para_consultar.upper()}")
    print(f"URL: {url_direta}")
    print("=====================================================")

    try:
        driver.get(url_direta)
        print("Aguardando resultados...")

        XPATH_TABELA_1 = '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]'
        XPATH_TABELA_2 = '//*[@id="layout"]/div[2]/div/div[1]/div/table[3]'

        print("\n--- Tabela 1: Dados do Veículo ---")
        processar_e_imprimir_tabela(driver, XPATH_TABELA_1)

        print("\n--- Tabela 2: Tabela FIPE ---")
        processar_e_imprimir_tabela(driver, XPATH_TABELA_2)

    except Exception as e:
        print(f"--- FALHA NA CONSULTA ---")
        print(f"Erro: {e}")
    finally:
        driver.quit()
        print("\nNavegador virtual fechado.")

# Garante que a função main seja executada quando o script for chamado
if __name__ == "__main__":
    main()
