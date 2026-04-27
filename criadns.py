import sys

def gerar_dns():
    # Verifica se os argumentos foram passados (GCA e IP/Rede)
    if len(sys.argv) < 3:
        print("\n[!] Erro: Faltam argumentos.")
        print("Uso: python3 criadns.py <GCA> <IP_REDE/MASCARA>")
        print("Exemplo: python3 criadns.py GCA-VIVO-RJOBAR001 152.255.36.212/29\n")
        return

    gca = sys.argv[1].upper()
    entrada_ip = sys.argv[2]

    # Trata o IP: separa o endereço da máscara se houver
    ip_rede = entrada_ip.split('/')[0]
    mascara = entrada_ip.split('/')[1] if '/' in entrada_ip else "30"

    try:
        # Quebra o IP em octetos para fazer a matemática no último
        octetos = ip_rede.split('.')
        base_ip = f"{octetos[0]}.{octetos[1]}.{octetos[2]}"
        final_rede = int(octetos[3])
        
        # Lógica de IPs: Rede + 1 (GW), Rede + 2 (VOD), Rede + 3 (LIVE)
        ip_gw = f"{base_ip}.{final_rede + 1}"
        ip_vod = f"{base_ip}.{final_rede + 2}"
        ip_live = f"{base_ip}.{final_rede + 3}"
    except Exception:
        print("\n[!] Erro: Formato de IP inválido. Use algo como 152.255.36.212\n")
        return

    # Lógica de identificação (GTCE vs EDGE)
    partes = gca.split('-')
    if "GTCE" in gca:
        tipo = "gtce"
        parceiro = partes[2].lower()
        local_raw = partes[3]
    else:
        tipo = "edge"
        parceiro = partes[1].lower()
        local_raw = partes[2]

    # Extração de numeração, estado e cidade
    num = gca[-2:]
    estado = local_raw[0:2].lower()
    cidade = local_raw[2:5].lower()
    
    # Montagem do domínio conforme seu padrão (.video)
    dominio = f"{tipo}-{parceiro}-{cidade}-{estado}.video"

    # Saída formatada no terminal
    print("\n" + "="*60)
    print(f"RELATÓRIO DE CONFIGURAÇÃO DNS")
    print(f"GCA Origem: {gca}")
    print(f"Rede Base:  {ip_rede}/{mascara}")
    print("-" * 60)
    print(f"Gateway:    {ip_gw}")
    print(f"VOD-{num}:     vod-{num}.{dominio}  -> {ip_vod}")
    print(f"LIVE-{num}:    live-{num}.{dominio} -> {ip_live}")
    
    if mascara == "29":
        print("-" * 60)
        print(f"DICA: IPs .{final_rede+4} até .{final_rede+6} estão livres nesta /29.")
    print("="*60 + "\n")

if __name__ == "__main__":
    gerar_dns()
