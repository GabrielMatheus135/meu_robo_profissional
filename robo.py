import datetime
import pandas as pd
import os

#Simulação de coleta de dados
def coletar_dados():
    return[
        {"data": datetime.date.today(), "evento": "Processamento finalizado", "status": "OK"},
    ]

#salvar em um csv
def salvar_relatorio(dados):
    os.makedirs('dados', exist_ok=True)

    df = pd.DataFrame(dados)
    df.to_csv('dados/relatorio.csv', index=False)

    print("Relatório salvo com sucesso!")

#Execução principal
if __name__ == "__main__":
    print("Iniciando robô...")
    dados = coletar_dados()
    salvar_relatorio(dados)