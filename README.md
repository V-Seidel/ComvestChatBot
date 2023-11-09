# ComvestChatBot

Este código implementa um chatbot que fornece respostas a perguntas relacionadas ao vestibular da Unicamp 2024. O chatbot utiliza a base de dados da Unicamp 2024 como fonte de informações. A seguir, vou fornecer uma documentação detalhada sobre o código:

## Parte 1: Configuração e Inicialização ## 
* Importações: O código começa importando os módulos e bibliotecas necessários. Alguns dos principais módulos importados incluem os, módulos do Langchain para carregar documentos, dividir texto, processar embeddings e criar um modelo de chat, bem como o módulo Streamlit para a interface do usuário.

* Configuração da Chave da API OpenAI: A chave da API OpenAI é definida no ambiente como OPENAI_API_KEY.

## Parte 2: Preparação dos Dados ##
* Carregamento da Base de Dados da Unicamp: A base de dados da Unicamp é carregada a partir de uma URL específica (https://www.pg.unicamp.br/norma/31594/0) usando o WebBaseLoader do Langchain.

* Divisão de Texto em Chunks: Os documentos da base de dados são divididos em chunks (pedaços) de 1000 caracteres, com um overlap de 200 caracteres, usando o RecursiveCharacterTextSplitter. Essa etapa visa preparar os documentos para uma pesquisa mais eficaz.

* Criação de um Vector Store: Os embeddings da OpenAI são usados para criar um vector store a partir dos documentos divididos. O vector store é nomeado "unicamp_base" e é persistido em um diretório específico.

## Parte 3: Configuração do Chatbot ##
* Template para o Prompt: É definido um template para o prompt usado pelo chatbot. O template inclui placeholders para contexto, histórico da conversa e a pergunta do usuário.

* Configuração do Modelo de Chat: O chatbot utiliza o modelo de linguagem GPT-3.5-turbo da OpenAI com uma temperatura de 0.3. O modelo é configurado com um template de prompt.

* Configuração da Memória do Chatbot: O chatbot usa a ConversationBufferMemory para armazenar o histórico da conversa.

* Criação do Chatbot: O chatbot é criado usando a cadeia de busca "RetrievalQA". Ele usa o modelo de chat, o vector store, o prompt e a memória configurados anteriormente.

## Parte 4: Interface do Usuário (Frontend) ##
* Configuração da Página do Streamlit: A página do Streamlit é configurada com o título "Unicamp Vestibular 2024".

* Inicialização do Histórico de Conversa: O histórico de conversa é inicializado na sessão do Streamlit.

* Exibição da Mensagem Inicial: Uma mensagem inicial é exibida na interface do chatbot.

* Exibição de Mensagens Anteriores: Se houver mensagens no histórico, elas são exibidas na interface do chatbot.

* Processamento da Entrada do Usuário: O chatbot aguarda a entrada do usuário e, quando a entrada é fornecida, processa a pergunta do usuário.

* Exibição da Resposta do Chatbot: A resposta do chatbot é exibida na interface, e a mensagem é adicionada ao histórico.

## Parte 5: Teste da Precisão do Chatbot ##
* Carregamento do Avaliador: Um avaliador é carregado para avaliar a precisão das respostas do chatbot com base em critérios específicos.

* Perguntas de Teste e Respostas Esperadas: Um conjunto de perguntas de teste e suas respostas esperadas é definido.

* Geração de Previsões: O chatbot é usado para gerar respostas para as perguntas de teste.

* Comparação de Respostas: As respostas geradas pelo chatbot são comparadas com as respostas esperadas, e os resultados são exibidos.
