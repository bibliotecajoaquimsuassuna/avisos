import time
import webbrowser
from datetime import datetime, date

# ==================================================
# CONFIGURAÇÕES PRINCIPAIS
# ==================================================

# Tempo (em segundos) entre cada verificação de horário
INTERVALO_VERIFICACAO = 30

# Lista de avisos
# Cada item é um dicionário com:
# - horario: no formato "HH:MM"
# - url: página que será aberta naquele horário
lista_avisos = [
    {
        "horario": "17:45",
        "url": "https://bibliotecajoaquimsuassuna.github.io/libpage/jogos.html"
    },
    {
        "horario": "18:00",
        "url": "https://bibliotecajoaquimsuassuna.github.io/libpage/nogames.html"
    },
    {
        "horario": "19:45",
        "url": "https://bibliotecajoaquimsuassuna.github.io/libpage/warning.html"
    }
]

# ==================================================
# PROGRAMA
# ==================================================

def main():
    # Guarda quais avisos já foram executados no dia
    lista_avisos_executados = set()

    # Guarda a data atual para detectar troca de dia
    data_atual = date.today()

    # Loop infinito (o app roda enquanto o PC estiver ligado)
    while True:
        agora = datetime.now()
        hora_atual = agora.strftime("%H:%M")

        # ----------------------------------------------
        # RESET DIÁRIO (à meia-noite)
        # ----------------------------------------------
        if date.today() != data_atual:
            lista_avisos_executados.clear()
            data_atual = date.today()

        # ----------------------------------------------
        # VERIFICA OS AVISOS
        # ----------------------------------------------
        for aviso in lista_avisos:
            horario = aviso["horario"]
            url = aviso["url"]

            # Identificador único do aviso no dia
            chave_aviso = f"{data_atual}_{horario}"

            # Se for o horário certo e ainda não abriu hoje
            if hora_atual == horario and chave_aviso not in lista_avisos_executados:
                webbrowser.open(url)
                lista_avisos_executados.add(chave_aviso)

        # Aguarda antes de verificar novamente
        time.sleep(INTERVALO_VERIFICACAO)

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
