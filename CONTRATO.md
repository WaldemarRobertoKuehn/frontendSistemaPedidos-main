# Rascunho de contrato da tela

## 1. Dados que a tela exibe

| Campo | Tipo | Onde aparece |
|---|---|---|
| Nome da categoria | texto | Título de cada seção do cardápio e rótulo do filtro de categorias |
| Ícone da categoria | texto | Ao lado do título da seção e no filtro de categorias; também pode aparecer no lugar da imagem do produto |
| Nome do produto | texto | Cartão do produto, itens do carrinho e itens de um pedido |
| Descrição do produto | texto | Cartão do produto |
| Preço do produto | número | Cartão do produto |
| Imagem do produto | texto | Imagem do cartão do produto e do item no carrinho |
| Produto em destaque | booleano | Selo “Mais pedido” no cartão do produto quando o valor é verdadeiro |
| Quantidade de um produto | número | Controle de quantidade no cartão, no carrinho e em cada item do pedido |
| Quantidade total de itens | número | Contador da navegação, barra do carrinho e resumo do carrinho |
| Total do carrinho | número | Barra do carrinho e rodapé do carrinho |
| Nome do cliente | texto | Campo de preenchimento do carrinho e cabeçalho do cartão de pedido |
| Tipo de consumo | texto | Opções “Comer aqui” ou “Para viagem” no carrinho e metadados do cartão de pedido |
| Observação | texto | Campo opcional do carrinho e texto do cartão de pedido quando preenchido |
| Número do pedido | número | Identificação do pedido e mensagens de confirmação/status |
| Data e hora de criação | texto | Metadados do cartão de pedido |
| Itens do pedido | lista | Lista de produtos dentro do cartão de pedido |
| Preço unitário do item | número | Preço calculado de cada linha de item no cartão de pedido |
| Total do item | número | Preço de cada item no cartão de pedido e no carrinho |
| Total do pedido | número | Total no cartão de pedido |
| Status do pedido | texto | Etiqueta, filtro, seletor e botão de avanço do cartão de pedido |
| Cor do status | texto | Cor da etiqueta do status e do filtro correspondente |
| Contagem de pedidos por status | número | Contador de cada filtro de status |
| Quantidade total de pedidos | número | Subtítulo da tela “Pedidos” e filtro “Todos” |
| Quantidade de pedidos em andamento | número | Subtítulo da tela “Pedidos” |

## 2. Ações que o usuário dispara

| Ação na tela | O que deveria acontecer depois |
|---|---|
| Clicar em “Novo pedido” ou “Pedidos” na navegação | Trocar de tela e voltar ao início da página |
| Selecionar uma categoria do cardápio | Mostrar somente os produtos da categoria selecionada e voltar ao topo |
| Clicar no “+” de um produto | Adicionar uma unidade do produto ao carrinho e atualizar quantidades e total |
| Clicar no “+” do controle de quantidade | Aumentar em uma unidade a quantidade do produto |
| Clicar no “-” ou na lixeira do controle de quantidade | Diminuir uma unidade; remover o produto quando a quantidade chegar a zero |
| Clicar em “Ver pedido” ou no contador do carrinho | Abrir o carrinho |
| Clicar em fechar o carrinho, no fundo ou pressionar Escape | Fechar o carrinho |
| Clicar em “Limpar” | Remover todos os itens do carrinho |
| Preencher o nome do cliente | Manter o nome para o envio do pedido |
| Selecionar “Comer aqui” ou “Para viagem” | Manter o tipo de consumo escolhido para o envio |
| Preencher a observação | Manter a observação para o envio do pedido |
| Clicar em “Enviar pedido” | Validar o nome, criar o pedido, limpar o carrinho e mostrar confirmação; em caso de erro, mostrar aviso |
| Clicar em “Ver pedidos” no aviso de confirmação | Ir para a tela de pedidos |
| Selecionar um status nos filtros | Mostrar somente os pedidos com o status selecionado |
| Clicar em “Ver todos” quando não há resultado no filtro | Voltar a mostrar todos os pedidos |
| Clicar em atualizar pedidos | Buscar novamente os pedidos e os status, exibindo carregamento no botão |
| Escolher outro status no seletor de um pedido | Atualizar o status daquele pedido e mostrar um aviso |
| Clicar em “Iniciar preparo”, “Marcar pronto” ou “Marcar entregue” | Avançar o pedido para o próximo status e atualizar o cartão |
| Clicar em “Fazer um pedido” quando não há pedidos | Ir para a tela de novo pedido |
| Clicar em “Restaurar dados de exemplo” e confirmar | Apagar os pedidos feitos, restaurar os exemplos e recarregar a lista |
| Fechar um aviso | Remover o aviso da tela |

## 3. O que o servidor precisaria fazer

| Ação | Comportamento esperado do servidor |
|---|---|
| Carregar o cardápio | Entregar as categorias ordenadas e os produtos disponíveis para a tela montar o cardápio. |
| Adicionar, aumentar, diminuir ou remover itens do carrinho | Nenhuma operação de servidor é indicada no código; o carrinho é mantido na tela até o envio. |
| Limpar o carrinho | Nenhuma operação de servidor é indicada; apenas descartar os itens ainda não enviados. |
| Enviar pedido | Receber cliente, tipo, observação, ids dos produtos e quantidades; validar nome e itens, conferir disponibilidade, buscar os preços atuais, calcular o total, criar número e datas, iniciar com status “recebido” e devolver o pedido criado. |
| Carregar ou atualizar a tela de pedidos | Entregar a lista de pedidos, em ordem dos mais recentes, e a lista de status disponíveis. |
| Filtrar pedidos por status | Nenhuma operação obrigatória de servidor aparece no código; o filtro é aplicado na tela sobre a lista carregada. |
| Alterar o status pelo seletor ou pelo botão de avanço | Validar o novo status, localizar o pedido, atualizar o status e a data de atualização e devolver o pedido atualizado. |
| Restaurar dados de exemplo | ? Repor os pedidos iniciais definidos pelo projeto e devolver a lista resultante; o código atual faz isso localmente, sem uma operação de servidor. |
| Atualizar pedidos em outra aba | ? Notificar ou permitir uma nova consulta quando outro cliente alterar pedidos; o código atual observa mudanças do armazenamento local. |
| Exibir avisos, abrir/fechar telas e carrinho | Nenhuma operação de servidor é indicada; são comportamentos da interface. |

## 4. Dúvidas para o professor

- ? O campo “nome do cliente” representa uma identificação livre ou deveria seguir alguma regra de cadastro?
- ? O tipo de consumo aceita somente “Comer aqui” e “Para viagem”, como no código, ou haverá outras opções?
- ? O servidor deve impedir alteração de status para uma etapa que não seja a próxima da sequência?
- ? Usuários poderiam alterar manualmente qualquer status, inclusive voltar para um status anterior?
- ? Quem pode alterar status e restaurar os dados de exemplo?
- ? A restauração de dados de exemplo deve existir no sistema final ou serve apenas para demonstração?
- ? O servidor deve enviar atualizações em tempo real, ou a atualização manual é suficiente?
- ? O produto precisa ter limite máximo de quantidade por pedido? O código não define esse limite.
- ? Como o sistema deve tratar um produto que fique indisponível depois de ser adicionado ao carrinho? O código só valida isso no envio.
- ? O servidor deve aceitar observação vazia e qual é a regra de tamanho para esse campo? A tela limita a 140 caracteres, mas não há regra de servidor explícita.
- ? O número do pedido deve seguir a sequência mostrada nos dados de exemplo ou obedecer a outra regra?
- ? Datas e horários devem ser exibidos no fuso local do estabelecimento ou em outro fuso?
- ? “Entregue” e “Cancelado” são sempre estados finais? Isso é indicado pelo campo `finalizado`, mas a regra de negócio não foi explicada.
- ? O total deve sempre ser calculado pelo servidor a partir dos preços atuais, mesmo quando o preço mudar depois de o item entrar no carrinho?