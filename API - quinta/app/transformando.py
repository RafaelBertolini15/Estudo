from datetime import datetime

def transformar_dados(data):

    jogos = []

    for item in data["matches"]:
        grupo = item.get("group")
        if grupo is None:
            grupo = "N/A"

        estadio = item.get("venue")
        if estadio is None:
            estadio = "Não informado."

        data_original = item["utcDate"]
        dataformatada = datetime.strptime(
            data_original, "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%d/%m/%Y %H:%M")

        jogos.append({
            "id": item["id"],
            "grupo": grupo,
            "mandante": item["homeTeam"]["name"],
            "visitante": item["awayTeam"]["name"],
            "estadio": estadio,
            "data": dataformatada,
            "status": item["status"]
        })

    return jogos
