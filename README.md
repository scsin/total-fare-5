# Projeto cálculo de fatura

Em uma empresa de telefonia existe um software responsável pela tarifação das ligações, ele recebe um relatório com as ligações e calcula o valor da fatura de cada cliente, baseado nas regras de tarifação diurna ou noturna.
    
    Tarifação:
    Diurna - entre 6h00 e 22h00 :
        * Encargo permanente: R $ 0,36 (encargos fixos que são usados ​​para pagar o custo da conexão);
        * Taxa de ligação / minuto: R $ 0,09 (não há cobrança fracionada. *A cobrança se aplica a cada ciclo concluído de 60 segundos)*.
    Noturna - entre 22h00 e 6h00:
        * Taxa permanente: R $ 0,36
        * Taxa de ligação / minuto: R $ 0,00

Classificar as ligações por número de origem e agrupá-las com o valor total das ligacões feitas por esse número. 
Complete o método *classify_by_phone_number* que recebe por parâmetro um relatório em forma de lista de dicionários.
Os horários de início e fim das ligacões estão no formato timestamp e os números de telefone em strings, conforme a estrutura abaixo.

    records = [
        {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
        {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821}
    ]

Com o algoritmo apropriado, retorne uma lista contendo um dicionário com duas chaves: `source`  e `total` para cada número de origem, ordenado pelo maior valor.
O valor total deve ser arredondado em 2 casas decimais.

    Ex retorno 
    [
        {'source': '48-996355555', 'total': 234.89}, 
        {'source': '41-885633788', 'total': 124.89}, 
    ]
