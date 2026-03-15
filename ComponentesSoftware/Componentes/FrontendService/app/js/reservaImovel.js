// LISTA DE IMÓVEIS PARA RESERVA
const listaImoveis = document.getElementById("listaImoveis");
// VERIFICA SE O CLIENTE ESTÁ LOGADO
const cliente = JSON.parse(localStorage.getItem("clienteLogado"));

// traz as informações do cliente logado para o console (para depuração)
console.log("Cliente Logado:", cliente);

// SE O CLIENTE NÃO ESTIVER LOGADO, REDIRECIONA PARA A PÁGINA DE LOGIN
if (!cliente) {
    alert("Você precisa estar logado para acessar esta página.");
    window.location.href = "./login.html";
}

// FUNÇÃO PARA BUSCAR IMÓVEIS DISPONÍVEIS PARA RESERVA
async function buscarImoveis(){

    try{
        // URL DO SERVIÇO DE GERENCIAMENTO DE BENS PARA OBTER A LISTA DE IMÓVEIS
        const url = "http://localhost:8002/gerenciar-bens/imoveis/";
        // LOG PARA VER A URL GERADA (PARA DEPURAÇÃO)
        console.log("URL Generate: " + url);

        // FAZ A REQUISIÇÃO PARA O SERVIÇO E OBTÉM A RESPOSTA
        const response = await fetch(url);
        // VERIFICA SE A RESPOSTA FOI BEM-SUCEDIDA
        const imoveis = await response.json();

        // LOG PARA VER A LISTA DE IMÓVEIS OBTIDA (PARA DEPURAÇÃO)
        imoveis.forEach(imovel => {const card = document.createElement("div");
            // ADICIONA A CLASSE "CARD" PARA ESTILIZAÇÃO
            card.className = "card";
            // PREENCHE O CONTEÚDO DO CARD COM AS INFORMAÇÕES DO IMÓVEL
            card.innerHTML = `
                <h3>${imovel.endereco}, ${imovel.numero}</h3>
                <p><strong>Cidade:</strong> ${imovel.cidade}</p>
                <p><strong>Estado:</strong> ${imovel.estado}</p>
                <p><strong>Bairro:</strong> ${imovel.bairro}</p>
                <p><strong>Complemento:</strong> ${imovel.complemento}</p>
                <p><strong>Comodos:</strong> ${imovel.qtde_comodos}</p>
                <p><strong>Tamanho:</strong> ${imovel.metros_quadrados} m²</p>
                <p><strong>Valor:</strong> R$ ${imovel.valor} / Dia </p>
                <button onclick="reservarImovel('${imovel._id}')">Reservar</button>
            `;
            // ADICIONA O CARD À LISTA DE IMÓVEIS NA PÁGINA
            listaImoveis.appendChild(card);
        });
    }catch (erro) {
        // LOG DE ERRO PARA VER O QUE DEU ERRADO AO CARREGAR OS IMÓVEIS
        console.error("Erro ao carregar imóveis:", erro);
    }
  
}
// FUNÇÃO PARA RESERVAR UM IMÓVEL
async function reservarImovel(imovelId) {
    try {
        // LOG PARA VER O CLIENTE LOGADO E O ID DO IMÓVEL QUE ESTÁ SENDO RESERVADO (PARA DEPURAÇÃO)
        console.log("Cliente Logado:", cliente);
        // LOG PARA VER O ID DO IMÓVEL QUE ESTÁ SENDO RESERVADO (PARA DEPURAÇÃO)
        console.log("Imóvel ID:", imovelId);
        
        // EXTRAI AS INFORMAÇÕES NECESSÁRIAS DO CLIENTE LOGADO E DAS DATAS DE RESERVA
        const clienteCPF = cliente.cpf;
        const clienteNome = cliente.nome_completo;
        const data_inicio = document.getElementById("data_inicio").value;
        const data_fim = document.getElementById("data_fim").value;
        
        // url DO SERVIÇO DE GERENCIAMENTO DE RESERVAS PARA REALIZAR A RESERVA DO IMÓVEL, COM OS PARÂMETROS NECESSÁRIOS
        const url = 'http://localhost:8003/gerenciar-reserva/reservar-imovel/?cpf_cliente='
            +encodeURIComponent(clienteCPF)+
            '&nome_cliente='+encodeURIComponent(clienteNome)+
            '&id_imovel='+encodeURIComponent(imovelId)+
            '&data_inicio='+encodeURIComponent(data_inicio)+
            '&data_fim='+encodeURIComponent(data_fim);

        // LOG PARA VER A URL GERADA PARA A REQUISIÇÃO DE RESERVA (PARA DEPURAÇÃO)
        console.log("URL Generate: " + url);

        // FAZ A REQUISIÇÃO PARA O SERVIÇO DE GERENCIAMENTO DE RESERVAS PARA REALIZAR A RESERVA DO IMÓVEL
        const response = await fetch(url, {method: "POST",headers: {"Content-Type": "application/json"}});

        // VERIFICA SE A RESPOSTA FOI BEM-SUCEDIDA
        const result = await response.json();
        console.log("Response:", result);
        if (result.error || result.erro) {
            // LOG DE ERRO PARA VER O QUE DEU ERRADO NA RESERVA
            alert("Erro ao reservar imóvel: " + result.error || result.erro);
        } else {
            // LOG DE SUCESSO PARA VER O RESULTADO DA RESERVA
            alert("Imóvel reservado com sucesso!");
        }   
    } catch (erro) {
        // LOG DE ERRO PARA VER O QUE DEU ERRADO AO TENTAR RESERVAR O IMÓVEL
        console.error("Erro ao reservar imóvel:", erro);
        alert("Erro ao reservar imóvel. Por favor, tente novamente.");
    }
}

// FUNÇÃO PARA REALIZAR O LOGOUT DO CLIENTE
function logout() {
    // REMOVE AS INFORMAÇÕES DO CLIENTE LOGADO DO LOCAL STORAGE PARA REALIZAR O LOGOUT
    localStorage.removeItem("clienteLogado");
    alert("Logout bem-sucedido!");
    window.location.href = "./login.html";
}

buscarImoveis();

