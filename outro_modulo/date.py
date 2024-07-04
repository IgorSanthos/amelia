def date ():
    from datetime import datetime, timedelta
    # Data atual
    data_atual = datetime.now()
    # Primeiro dia do mês atual
    primeiro_dia_mes_atual = data_atual.replace(day=1)
    # Último dia do mês anterior
    ultimo_dia_mes_anterior = primeiro_dia_mes_atual - timedelta(days=1)
    # Formatação das datas
    primeiro_dia = primeiro_dia_mes_atual.strftime('%d')
    ultimo_dia_mes = ultimo_dia_mes_anterior.strftime('%d')
    mes_anterior = ultimo_dia_mes_anterior.strftime('%m')
    ano_anterior = ultimo_dia_mes_anterior.strftime('%Y')

    # Datas inicial e final
    data_inicial = f"{primeiro_dia}{mes_anterior}{ano_anterior}"
    data_final = f"{ultimo_dia_mes}{mes_anterior}{ano_anterior}"
    return data_inicial, data_final