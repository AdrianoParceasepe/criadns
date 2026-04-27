# Automação de DNS para Vídeo (CriaDNS)

Este script automatiza a geração de nomes de host DNS para infraestrutura de vídeo, seguindo os padrões de nomenclatura para nós **Edge** e **GTCE**.

## 💡 O que o script faz?

1.  **Identificação Automática:** Deteta se o servidor é `gtce` ou `edge` com base no nome do GCA.
2.  **Lógica de Localização:** Extrai automaticamente o Estado e a Cidade do código do GCA.
3.  **Numeração de Instância:** Mapeia o final do nome da máquina (ex: `001`) para a numeração do serviço (`vod-01` / `live-01`).
4.  **Cálculo de IP Incremental:** Você fornece o IP do VOD e o script calcula automaticamente o IP do LIVE (VOD + 1).

## 🚀 Como usar

Dê permissão de execução ao script:
```bash
chmod +x criadns.sh

Exemplo 
./criadns.sh GCA-VIVO-RJOBAR001 152.255.36.214

Exemplo de saida
--------------------------------------------------
DNS CONFIGURADO PARA: GCA-VIVO-RJOBAR001
VOD-01:  vod-01.edge-vivo-bar-rj.video  -> 152.255.36.214
LIVE-01: live-01.edge-vivo-bar-rj.video -> 152.255.36.215
--------------------------------------------------

Instalação

git clone [https://github.com/AdrianoParceasepe/criadns.git](https://github.com/AdrianoParceasepe/criadns.git)

Baixar apenas o script:

curl -O [https://raw.githubusercontent.com/AdrianoParceasepe/criadns/main/criadns.sh](https://raw.githubusercontent.com/AdrianoParceasepe/criadns/main/criadns.sh)
