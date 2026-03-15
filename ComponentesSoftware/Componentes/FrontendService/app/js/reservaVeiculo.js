// lista os veículos disponíveis para reserva e permite que o cliente faça uma reserva selecionando um veículo e informando as datas de início e fim da reserva
const listaVeiculos = document.getElementById("listaVeiculos");
// RECUPERA AS INFORMAÇÕES DO CLIENTE LOGADO DO LOCAL STORAGE PARA USAR NAS RESERVAS
const cliente = JSON.parse(localStorage.getItem("clienteLogado"));

// VERIFICA SE O CLIENTE ESTÁ LOGADO, CASO CONTRÁRIO REDIRECIONA PARA A PÁGINA DE LOGIN
console.log("Cliente Logado:", cliente);
if (!cliente) {
    alert("Você precisa estar logado para acessar esta página.");
    window.location.href = "./login.html";
}

// FUNÇÃO PARA BUSCAR OS VEÍCULOS DISPONÍVEIS PARA RESERVA E EXIBI-LOS NA PÁGINA
async function buscarVeiculos(){

    try{
        // URL DO SERVIÇO DE GERENCIAMENTO DE BENS PARA OBTER A LISTA DE VEÍCULOS
        const url = "http://localhost:8002/gerenciar-bens/veiculos/";
        // LOG PARA VER A URL GERADA (PARA DEPURAÇÃO)
        console.log("URL Generate: " + url);

        // FAZ A REQUISIÇÃO PARA O SERVIÇO E OBTÉM A RESPOSTA
        const response = await fetch(url);
        // VERIFICA SE A RESPOSTA FOI BEM-SUCEDIDA
        const veiculos = await response.json();
        console.log("Veículos recebidos:", veiculos);

        // cria os cards para cada veículo e os adiciona à página
        veiculos.forEach(veiculo => {const card = document.createElement("div");
            // ADICIONA A CLASSE "CARD" PARA ESTILIZAÇÃO
            card.className = "card";

            // PREENCHE O CONTEÚDO DO CARD COM AS INFORMAÇÕES DO VEÍCULO, INCLUINDO UM BOTÃO PARA RESERVAR O VEÍCULO
            card.innerHTML = `
                <h3>${veiculo.marca} ${veiculo.modelo}</h3>
                <p><strong>Ano:</strong> ${veiculo.ano}</p>
                <p><strong>Valor:</strong> R$ ${veiculo.valor} / Dia </p>
                <p><strong>Localização:</strong> ${veiculo.endereco}, ${veiculo.bairro}, ${veiculo.cidade}, ${veiculo.estado}</p>
                <button onclick="reservarVeiculo('${veiculo._id}')">Reservar</button>
            `;

            // ADICIONA O CARD À LISTA DE VEÍCULOS NA PÁGINA
            listaVeiculos.appendChild(card);
        });
    }catch (erro) {
        // LOG DE ERRO PARA VER O QUE DEU ERRADO AO CARREGAR OS VEÍCULOS
        console.error("Erro ao carregar veículos:", erro);
    }
  
}
// FUNÇÃO PARA REALIZAR A RESERVA DE UM VEÍCULO, ENVIANDO AS INFORMAÇÕES NECESSÁRIAS PARA O SERVIÇO DE GERENCIAMENTO DE RESERVAS
async function reservarVeiculo(veiculoId) {
    try {
        // LOG PARA VER O CLIENTE LOGADO E O ID DO VEÍCULO QUE ESTÁ SENDO RESERVADO (PARA DEPURAÇÃO)
        console.log("Cliente Logado:", cliente);
        console.log("Veículo ID:", veiculoId);
        
        // RECUPERA AS INFORMAÇÕES NECESSÁRIAS PARA REALIZAR A RESERVA, INCLUINDO O CPF E NOME DO CLIENTE, O ID DO VEÍCULO E AS DATAS DE INÍCIO E FIM DA RESERVA
        const clienteCPF = cliente.cpf;
        const clienteNome = cliente.nome_completo;
        const data_inicio = document.getElementById("data_inicio").value;
        const data_fim = document.getElementById("data_fim").value;
       
        // URL DO SERVIÇO DE GERENCIAMENTO DE RESERVAS PARA REALIZAR A RESERVA DO VEÍCULO, COM OS PARÂMETROS NECESSÁRIOS
        const url = 'http://localhost:8003/gerenciar-reserva/reservar-veiculo/?cpf_cliente='
            +encodeURIComponent(clienteCPF)+
            '&nome_cliente='+encodeURIComponent(clienteNome)+
            '&id_veiculo='+encodeURIComponent(veiculoId)+
            '&data_inicio='+encodeURIComponent(data_inicio)+
            '&data_fim='+encodeURIComponent(data_fim);
        // LOG PARA VER A URL GERADA PARA A REQUISIÇÃO DE RESERVA (PARA DEPURAÇÃO)
        console.log("URL Generate: " + url);
        // FAZ A REQUISIÇÃO PARA O SERVIÇO DE GERENCIAMENTO DE RESERVAS PARA REALIZAR A RESERVA DO VEÍCULO
        const response = await fetch(url, {method: "POST"});

        // VERIFICA SE A RESPOSTA FOI BEM-SUCEDIDA
        const result = await response.json();
        console.log("Response:", result);
        if (result.error || result.erro) {
            // LOG DE ERRO PARA VER O QUE DEU ERRADO NA RESERVA
            alert("Erro ao reservar veículo: " + result.error || result.erro);
        } else {
            // LOG DE SUCESSO PARA VER O RESULTADO DA RESERVA
            alert("Veículo reservado com sucesso!");
        }   
    } catch (erro) {
        // LOG DE ERRO PARA VER O QUE DEU ERRADO AO TENTAR RESERVAR O VEÍCULO
        console.error("Erro ao reservar veículo:", erro);
        alert("Erro ao reservar veículo. Por favor, tente novamente.");
    }
}

// FUNÇÃO PARA REALIZAR O LOGOUT DO CLIENTE
function logout() {
    // REMOVE AS INFORMAÇÕES DO CLIENTE LOGADO DO LOCAL STORAGE PARA REALIZAR O LOGOUT
    localStorage.removeItem("clienteLogado");
    alert("Logout bem-sucedido!");
    window.location.href = "./login.html";
}

buscarVeiculos();