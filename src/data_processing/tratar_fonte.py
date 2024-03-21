import pandas as pd
from unidecode import unidecode
import csv
import logging

# Configurar o sistema de log
logging.basicConfig(filename='transformacao.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def transformar_csv(input_file):
    try:
        # Realiza as transformações no arquivo CSV
        df = pd.read_csv(input_file, encoding='latin1', sep=';')

        # Exclue a coluna "Tipo Trafego"
        df = df.drop("Tipo Trafego", axis=1)

        # Divide a coluna "Período de Tráfego" em duas colunas: "ano trafego" e "mes trafego"
        df['ano trafego'] = df['Período de Tráfego'].astype(str).str[:4]
        df['mes trafego'] = df['Período de Tráfego'].astype(str).str[4:]
        df['ano referencia'] = df['Periodo de Referência'].astype(str).str[:4]
        df['mes referencia'] = df['Periodo de Referência'].astype(str).str[4:]

        # Substitui caracteres especiais por caracteres normais
        # Substitui caracteres especiais nos nomes das colunas
        df = df.rename(columns={
            'Período de Tráfego': 'Periodo de Trafego',
            'mes trafego': 'mes trafego',
            'Periodo de Referência': 'Periodo de Referencia',
            'Valor Líquido Retornado': 'Valor Liquido Retornado'
        })

        # Mapeia o número do mês para o nome do mês
        meses = {
            '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
            '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
            '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
        }
        df['mes trafego'] = df['mes trafego'].map(meses)
        df['mes trafego'] = df['mes trafego'].str.replace('á', 'a').str.replace('ã', 'a').str.replace('ê', 'e').str.replace('í', 'i')
        df['mes referencia'] = df['mes referencia'].map(meses)
        df['mes referencia'] = df['mes referencia'].str.replace('á', 'a').str.replace('ã', 'a').str.replace('ê', 'e').str.replace('í', 'i')

        # Dicionário de mapeamento de meses por extenso para números
        meses_mapping = {
            'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6,
            'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12
        }

        # Cria as novas colunas 'mes trafego numeral' e 'mes referencia numeral' usando o mapeamento e converta para inteiros
        df['mes trafego numeral'] = df['mes trafego'].str.lower().map(meses_mapping).astype(int)
        df['mes referencia numeral'] = df['mes referencia'].str.lower().map(meses_mapping).astype(int)

        # Converte as colunas de texto em números
        columns_to_convert = ["Qtde Minutos", "Valor Liquido Retornado", "Valor Bruto Retornado", 
                              "Valor Bruto FI", "Valor Bruto ICMS FI"]

        df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')

        # Nome do arquivo de saída com sufixo "_transformado.xlsx"
        xlsx_output_file = 'fonte_transformado.xlsx'

        # Salva o DataFrame transformado em um novo arquivo XLSX
        df.to_excel(xlsx_output_file, index=False)

        logging.info(f'Transformações concluídas. Arquivo transformado salvo em {xlsx_output_file}')
    
    except Exception as e:
        logging.error(f'Erro na transformação: {str(e)}')

# Chama a função para realizar as transformações no arquivo "fonte_v4.csv" na pasta atual
transformar_csv("fonte.csv")