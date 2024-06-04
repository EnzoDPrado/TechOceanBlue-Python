 # Projeto Find-Bot

### Grupo:
Rafael Duarte de Freitas, RM: 558644 <br>
Enzo Diógenes do Prado, RM: 555062

---

### Descrição do Projeto

O projeto Find-Bot tem como objetivo identificar e contabilizar resíduos flutuantes nos oceanos, além de monitorar a temperatura das águas. A solução utiliza um sistema baseado no ESP32, equipado com sensores ultrassônicos, de inclinação e DHT22. 

- **Sensor ultrassônico**: Detecta resíduos próximos a uma distância de até 10 cm.
- **Sensor de inclinação**: Verifica mudanças bruscas de inclinação nos 5 segundos seguintes para diferenciar resíduos de ondas.
- **Sensor DHT22**: Mede a temperatura da água e verifica desvios da temperatura normal.

Os dados coletados (localização, temperatura) são enviados a um servidor, permitindo monitorar a quantidade e localização dos resíduos nos oceanos, bem como analisar a temperatura média da água. Todas as informações são exibidas em tempo real em um website.

### Instruções de Uso

Este projeto simula o comportamento do Find-Bot, permitindo ao usuário explorar diferentes oceanos e contabilizar resíduos encontrados. Siga as etapas abaixo para executar o código:

1. Certifique-se de ter o Python instalado em seu sistema.
2. Salve o código fornecido em um arquivo chamado `techOceanBlue.py`.
3. Execute o script no terminal ou ambiente de desenvolvimento com o comando:
   ```sh
   python techOceanBlue.py
   ```

4. Siga as instruções exibidas para selecionar os oceanos a serem explorados e ver os resultados.

### Requisitos

- Python 3.x
- Bibliotecas: `time`, `random`

### Dependências

O código utiliza as bibliotecas padrão do Python, sem necessidade de instalação de pacotes adicionais.

### Funcionalidades

- **Exploração de Oceanos**: O usuário pode selecionar entre o Oceano Atlântico, Índico e Pacífico para explorar.
- **Identificação de Resíduos**: O Find-Bot simula a detecção de resíduos no oceano, classificando-os como "Pedra", "Peixe" ou "Lixo".
- **Resumo da Exploração**: Ao final de cada exploração, o script exibe um resumo dos resíduos encontrados e a quantidade de lixo contabilizada.

### Detalhes Técnicos

- **Sensores e Simulação**:
  - A simulação de resíduos é feita utilizando a biblioteca `random` para gerar uma lista aleatória de resíduos encontrados em cada exploração.
  - A função `findResidues` processa os resíduos detectados, contabilizando o lixo encontrado.

- **Interface com o Usuário**:
  - O script solicita ao usuário que selecione os oceanos a serem explorados e decide se deseja continuar ou encerrar a exploração após cada etapa.
  - As entradas do usuário são validadas para garantir opções válidas.

### Exemplo de Uso

1. Iniciar a exploração:
   ```
   |||||||||||||||||||||||||||||||||
    |||| FIND-BOT INICIALIZADO ||||
   |||||||||||||||||||||||||||||||||
   
   1 - Oceano Atlântico
   2 - Oceano Índico
   3 - Oceano Pacífico
   Selecione um oceano para explorar com o find-bot:
   ```

2. Exploração e Resumo:
   ```
   Resíduo encontrado!
   Resíduo encontrado!
   Foram encontrados os seguintes resíduos:
   1 - Pedra
   2 - Lixo
   E a seguinte quantidade de lixos: 1
   ```

3. Encerrar ou continuar a exploração:
   ```
   Deseja continuar explorando ou deseja encerrar?
   1 - Continuar Explorando
   2 - Encerrar
   ```

### Conclusão

O projeto Find-Bot é uma solução eficiente para monitoramento ambiental, proporcionando dados valiosos sobre resíduos oceânicos e temperaturas das águas. Esta simulação demonstra como o sistema pode ser utilizado para explorar e analisar diferentes oceanos, contribuindo para a preservação do meio ambiente marinho.