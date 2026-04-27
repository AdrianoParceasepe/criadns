#!/bin/bash

GCA=$1
IP_VOD=$2

if [ -z "$GCA" ] || [ -z "$IP_VOD" ]; then
    echo "Uso: ./criadns.sh GCA-VIVO-RJOBAR001 152.255.36.214"
    exit 1
fi

# 1. Identifica se é GTCE ou EDGE e extrai o parceiro e local
if [[ "$GCA" == *"GTCE"* ]]; then
    TIPO="gtce"
    PARCEIRO=$(echo $GCA | cut -d'-' -f3 | tr '[:upper:]' '[:lower:]')
    LOCAL_RAW=$(echo $GCA | cut -d'-' -f4)
else
    TIPO="edge"
    PARCEIRO=$(echo $GCA | cut -d'-' -f2 | tr '[:upper:]' '[:lower:]')
    LOCAL_RAW=$(echo $GCA | cut -d'-' -f3)
fi

# 2. Extrai a numeração final da máquina (ex: 001 -> 01)
NUM=$(echo ${GCA: -2})

# 3. Extrai Estado e Cidade (ex: RJ e OBA)
ESTADO=$(echo ${LOCAL_RAW:0:2} | tr '[:upper:]' '[:lower:]')
CIDADE=$(echo ${LOCAL_RAW:2:3} | tr '[:upper:]' '[:lower:]')

# 4. Lógica do IP (VOD par, LIVE = VOD + 1)
BASE_IP=$(echo $IP_VOD | cut -d'.' -f1-3)
ULTIMO_OCTETO=$(echo $IP_VOD | cut -d'.' -f4)
IP_LIVE="$BASE_IP.$((ULTIMO_OCTETO + 1))"

# Domínio terminando apenas em .video
DOMINIO="$TIPO-$PARCEIRO-$CIDADE-$ESTADO.video"

echo "--------------------------------------------------"
echo "DNS CONFIGURADO PARA: $GCA"
echo "VOD-$NUM:  vod-$NUM.$DOMINIO  -> $IP_VOD"
echo "LIVE-$NUM: live-$NUM.$DOMINIO -> $IP_LIVE"
echo "--------------------------------------------------"
