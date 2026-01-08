# 🚀 Projeto Nexus

O **Nexus** é um projeto criado para gerenciar e servir dados de **componentes e suas séries temporais de simulação**. O projeto foi desenvolvido com foco em eficiência para lidar com **grandes volumes de dados**.

---

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python 
- **Banco de dados:** PostgreSQL
- **Framework:** FastAPI
- **Servidor ASGI:** Uvicorn
- **Containerização:** Docker e Docker Compose
- **Testes:** Pytest

---

## 📌 Objetivos do Projeto

* Disponibilizar endpoints REST para consulta de componentes.
* Retornar séries temporais de simulação volumosas.
* Avaliar estratégias para otimizar o tráfego de grandes payloads.
* Demonstrar boas práticas de arquitetura em camadas, testes automatizados e documentação.

---

## 🧱 Arquitetura (Visão Geral)

O projeto utiliza uma estrutura desacoplada para garantir manutenibilidade. Nesse MVP, foram criadas duas camadas:
* **Controller:** Camada de entrada (endpoints) e validação de parâmetros.
* **Repository:** Responsável pelo acesso e abstração dos dados.

---

## 📋 Pré-requisitos

- Docker
- Docker Compose

---

## 🕹️ Como Rodar o Projeto

Renomeie o arquivo `.env.example` para `.env` e ajuste as variáveis se achar necessário.


### Rodando separadamente 

```
$docker compose up [nome_do_servico] --build
```

Os serviços definidos no `docker-compose` são: *postgres*, *ingest*, *api-metadados* e *api-series*.  
A flag `--build` é necessária apenas para a criação das imagens.

A API de metadados depende do container do **PostgreSQL** e da **ingestão inicial dos dados**. Para seu correto funcionamento, ambos os serviços precisam estar disponíveis. Após a ingestão ser concluída com sucesso, não é necessário executá-la novamente.


### Rodando de forma conjunta:

```
$docker compose up --build
```

### Para parar os serviços:


```
$docker compose stop
```

## Para remover containers, volumes e todas as imagens do projeto

```
$docker compose down -v --rmi all
```

## 🧪 Testes automatizados

### API de Metadados
```
$docker compose run --rm api-metadados pytest tests/test_component.py -v
```

### API de Séries Temporais
```
$docker compose run --rm api-series pytest tests/test_time_series_simulation.py -v
```

## 📄 Documentação da API (Swagger)

API de Metadados: http://localhost:8000/docs

API de Séries Temporais: http://localhost:8001/docs

O Swagger é usado apenas para documentação das rotas e testes simples. Para a API de séries temporais, que retorna um arquivo de 144MB, recomenda-se o teste pelo terminal usando curl:

```
curl -w   -o /dev/null      -s      http://localhost:8001/components/1/simulation
```

Para avaliar o tempo de resposta total:

```
curl -w "\nTTFB: %{time_starttransfer}s\nTotal: %{time_total}s\nSize: %{size_download} bytes\n"      -o /dev/null      -s      http://localhost:8001/components/1/simulation
```

Para ver o download do arquivo direto no navegador, copiar e colar a url direto no navegador, após rodar a api-series:

```
http://localhost:8001/components/1/simulation
```


-----

Desenvolvido por : Elaine Dias Pires ❤️