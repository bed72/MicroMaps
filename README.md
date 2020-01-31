# MicroMaps
Microsserviço para obtenção de dados de arquivos .osm <span style="font-size: 100px">&#129497;&#127997;</span>


Tanto o Microsserviço quanto a api estão dentro do mesmo pacote Python,
porém executar individualmente cada um dos serviços!

Ter configurado no <i>host</i> em que será executado o codigo o:<br/>
<strong>Erlang </strong> <br/>
<strong>Rabbitmq </strong> <br/>
<strong>Python </strong> <br/>
<strong>Virtualenv </strong> <br/>
<strong>FastAPI </strong> <br/>
<strong>Nameko </strong> <br/>

<strong>Links:</strong> <span>&#128072;&#127998;</span><br/> 
<strong>(rabbitmq):</strong> https://www.rabbitmq.com/ <br/>
<strong>(erlang):</strong> https://www.erlang.org/<br/>
<strong>(nameko):</strong> https://www.nameko.io/<br/>
<strong>(fastapi):</strong> https://fastapi.tiangolo.com/features/<br/>

Também pode ser executado com <i>Django</i> e <i>Flask</i>, (realizar devidas configurações).<br/>

# Execução da API:<br/>
Navegue até a pasta <i>api</i> e execute o comando:<br/>

<strong>uvicorn api:app --reload</strong><br/>


# Execução do Microservice:<br/>

<strong>nameko run --config ./service.yaml microservice:MapsService</strong><br/>

Onde:<br/>
<strong>./service.yaml:</strong> E o nome do arquivo de configuração para rodar conexão com o <i>Rabbitmq</i> <br/>
<strong>microservice:</strong> E o nome do arquivo que conterá código <i>Nameko</i> <br/>
<strong>MapsService:</strong> E o nome da classe que conterá código <i>Nameko</i> <br/>
