# Teste-Fractal
Conjunto de códigos desenvolvidos para o processo seletivo na Fractal

O objetivo do teste era automatizar o download de dados de precipitação da NOAA(NOMADS) usando a ferramenta grib filters, analisando os resultados do modelo em algumas bacias hidrográficas brasileiras e comparando-os com alguns resultados fornecidos.

Apresenta-se os gráficos e figuras obtidos na pasta anexos, assim como os arquivos intermediários mencionados ao longo dos scripts, principais desafios e próximos passos.

# Considerações
Não foi feita a análise usando dados baixados em formato GRIB2 por duas razões:
1. Não foi encontrado na base de dados da NOAA informações meteorológicas que abrangessem dados de precipitação, tendo como base o modelo CFSV2, se limitando a outras variáveis (ver referência 1). Por essa razão, optou-se por usar os dados de precipitação disponibilizados em formato NETCDF4;
2. Por questões técnicas que ainda estou avaliando, não foi possível instalar algumas dependências importantes para análise dos dados em formato GRIB2, em especial as ferramentas wgrib (da NOAA/NOMADS), pynio e GDAL. Embora o GDAL tenha sudo utilizado, sua execução foi conduzida no ambiente Python do QGIS, onde a biblioteca já estava instalada. Apesar disso, apresenta-se o script para download automatizado dos dados GRIB2 (script 01) usando o Grib Filters da NOAA
3. A análise dos dados foi feita usando a anomalia, ao invés da precipitação. Não foi encontrado o dado de precipitação base para o modelo CSFV2, apenas a anomalia, e optou-se por converter os dados fornecidos para essa unidade. A comparação dos resultados, nesse caso, indica tendência a maior ou menor chuva em relação a uma precipitação de referência. Os valores absolutos devem ser avaliados com cautela, pois não pode ser feita a verificação dos valores de referência do modelo CFSV2.


# Descrição dos algoritmos (scripts)
## 01 - Download automatizado de dados GRIB2 da NOAA/NOMADS
Tem-se como entrada a data, no formado de string e AAAAMMDD. Realiza-se a tentativa de download para a resolução temporal de 6 horas do modelo (00, 06, 12 e 18 horas). Salva-se os arquivo os arquivos e imprime mensagens de erro, caso o download não seja bem sucedido, o que usualmente acontece quando o dado não está disponível.

## 02 - Preparação dos arquivos NETCDF
Os arquivos NETCDF, gerados pelo modelo CFSV2 e disponíveis para download na referência 3, incluem os dados de precipitação. Baixados manualmente, precisam ser processado antes de ser usados. Nota-se que os arquivos estão na projeção WGS84, em escala global, mas com longitudes na faixa de (0 - 360), e que tem como ponto de longitude zero aquele que deveria ser o -180 na projeção WGS correta. Portanto, transladou-se essas informações em 360 graus para esquerda, usando a biblioteca GDAL. Ilustração na pasta "arquivos_extra"

## 03 - Corte do arquivo NETCDF usando os shapefiles fornecidos
O arquivo NETCDF foi cortado para caca uma das bacias fornecidas, e convertido para o formato GEOTIFF, mais acessível que o NETCDF

## 04 - Processamento dos dados de precipitação e conversão em tabelas para cada bacia
Para comparar com os dados fornecidos, foi fieta a conversão dos dados pluviométricos, separados por bacia no item anterior, para tabelas. Para isso, filtrou-se a média de cada banda de cada bacia, representado a anomalia média na precipitação em cada mês (cada banda representa um mês, de novembro/2021 a abril/2020). Os dados E1, E2 e E3 representam as médias tendo como base, respectivamente, os dias  1-10, 20-20 e 20-30 do mês. Foi feita a média entre valores para obter o arquivo final.

O passo 4 encerra o pré-processamento dos arquivos vindos da NOAA/NOMADS, tendo finalizada a transformação dos arquivos NETCDF brutos em tabelas para a área de estudo

## 5 - Processamento dos dados fornecidos
a etapa de ETL dos dados fornecidos visou compatibilizá-los com os da NOAA/NOMADS, a abordagem escolhida sendo gerar uma única tabela para todos os dados. Essa abordagem simplifica o armazenamento das informações e seu uso com a biblioteca Pandas. Os dados foram convertidos em listas para cada bacia, adicionando-se a informação de ano e mês, para então serem concatenados em uma única tabela.

## 6 - Compatibilização das bases de dados
Os dados fornecidos e os gerados dos arquivos da NOAA/NOMADS tiveram seus campos e dimensões compatibilizados. Os nomes das colunas passaram a ser "Bacia", "Mes", "Ano", e "Anomalia" ou "Precipitação"

## 7 - Filtra dados para período em comum e plota gráficos
É feita a filtragem dos dados fornecido para o período de Novembro/2021 - Abril/2022, os 6 meses em comum com os dados da=o modelo CFSV2. É feito o cálculo da anomalia dos dados fornecidos (precipitação mensal - média da precipitação entre 1991 e 2020, mesmo critério sugerido pela NOAA).

# Principais desafios
O desenvolvimento da solução teve dois principais desafios: a acessibilidade dos dados e instalação dos pacotes.
O site da NOAA/NOMADS é pouco intuitivo, com as ferramentas e dados estruturados de forma pouco organizada. Em termos práticos, pode-se encontrar a mesma informação (ex.: arquivos grib2 e grib filters) em várias partes do site, não necessariamente relacionadas, dificultando o acesso aos dados. Adicionalmente, as informações disponíveis são explicadas de forma superficial ou confusa, complicando sua aplicação, além de frequentemente levarem para páginas não existentes ou outros sites. Destaco a dificuldade em acessar dados antigos, que permitiriam calcular as precipitações a partir das anomalias, e em acessar os dados de chuva. Nenhum dos arquivos GRIB2 parece ter a variáveis "Precipitação" ou "Anomalia", obrigando o uso do formato NETCDF. Por último, algumas das atualizações mostram datas antigas e links quebrados, e um site que, no geral, parece não ser muito bem mantido, apesar dos dados dos modelos serem atualizados.

Quanto as ferramentas utilizadas, a instalação do wgrib2, gdal e pynio se mostraram as mais desafiadoras, sendo que entre elas só foi possível concluir a instalação do wgrib2, que acabou não sendo usado pela dificuldade em achar os dados de precipitação nesse formato. Essas limitações levaram ao uso de soluções alternativas, como usar o console Python do QGIS para rodar o GDAL.

# Próximos passos
Caso tivesse mais tempo, acho que o ponto mais importante seria avaliar a disponibilidade dos dados de chuva no formato GRIB2, talvez entrando em contato com o pessoal da NOAA, para contornar a obrigatoriedade do uso das anomalias como base do estudo. Adicionalmente, refaria a instalação do Linux e insistiria em instalar as bibliotecas GDAL e pynio, para lidar com os dados de grid, aém da wgrib2. Acredito que come esses passos seria possível ter um maior grau de automatização, baixando os dados de chuva como proposto no script01, e tendo resultados mais coesos.

Adicionalmente, aprofundaria mais os estudos na aplicação desses dados em formato de grid e interpretação dos resultados, em especial as anomalias. Também passaria mais tempo avaliando as questões envolvidas nos resultados da Amazônia e Tiete, e características das suas séries fornecidas e shapefiles.

# Considerações finais
Os resultados mostraram boa correlação entre as anomalias para as bacias Grande, Iguaçu, e Uruguai, validando a aplicabilidade do modelo. A bacia Paranapanema também mostrou correlação, enquanto tocantins mostrou tendência parecida. As demais (Amazônia, Tiete) não mostraram correlação. Os dados simulados pelo modelo CFSV2 para a bacia do Tiete mostram anomalia igual a zero, indicando uma falha no método de análise ou no arquivo. Os resultados da Amazônia são os mais contraintuitivos - esperava-se maior correlação, por conta da área maior. Esse resultado pode indicar alguma falha no método aplicado e requer mais tempo de estudo para determinar qual dos resultados é o correto.


Referências:
1. https://nomads.ncep.noaa.gov/ - acesso ao dados NOAA/NOMADS.
2. https://nomads.ncep.noaa.gov/cgi-bin/filter_cfs_flx.pl?dir=%2Fcfs.20211031%2F12%2F6hrly_grib_01 - Dados gerados pelo modelo CFSV2 disponíveis para download
3. https://www.cpc.ncep.noaa.gov/products/CFSv2/CFSv2_body.html - Acesso aos dados de precipitação do modelo CFSV2
