import sys

def gerar_dns():
    # Verifica se você passou os argumentos (GCA e IP)
    if len(sys.argv) < 3:
        print("Uso: python3 criadns.py GCA-VIVO-RJOBAR001 152.255.36.214")
        return

    gca = sys.argv[1].upper()
    ip_vod = sys.argv[2]

    # 1. Identifica se é GTCE ou EDGE e extrai o parceiro e local
    partes = gca.split('-')
    
    if "GTCE" in gca:
        tipo = "gtce"
        parceiro = partes[2].lower()
        local_raw = partes[3]
    else:
        tipo = "edge"
        parceiro = partes[1].lower()
        local_raw = partes[2]

    # 2. Extrai a numeração (ex: 001 -> 01)
    num = gca[-2:]

    # 3. Extrai Estado e Cidade (ex: RJ e OBA)
    estado = local_raw[0:2].lower()
    cidade = local_raw[2:5].lower()

    # 4. Lógica do IP Incremental
    # Divide o IP pelos pontos, pega o último número, soma 1 e junta tudo de novo
    octetos = ip_vod.split('.')
    ultimo_octeto = int(octetos[3])
    ip_live = f"{octetos[0]}.{octetos[1]}.{octetos[2]}.{ultimo_octeto + 1}"

    # 5. Monta o domínio
    dominio = f"{tipo}-{parceiro}-{cidade}-{estado}.video"

    print("-" * 50)
    print(f"DNS CONFIGURADO PARA: {gca}")
    print(f"VOD-{num}:  vod-{num}.{dominio}  -> {ip_vod}")
    print(f"LIVE-{num}: live-{num}.{dominio} -> {ip_live}")
    print("-" * 50)

if __name__ == "__main__":
    gerar_dns()
