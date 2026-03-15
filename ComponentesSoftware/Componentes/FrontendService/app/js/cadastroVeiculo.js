// Verificar se o cliente está logado
const cliente = JSON.parse(localStorage.getItem("clienteLogado"));

// Se não estiver logado, redirecionar para a página de login
console.log("Cliente Logado:", cliente);
if (!cliente) {
    alert("Você precisa estar logado para acessar esta página.");
    window.location.href = "./login.html";
}

// Função para buscar o endereço com base no CEP
function buscarCep(){
    // Pega o valor do campo cep e armazena na variável cep
    let cep = document.getElementById("cep").value;

    // Cria a url para o fetch utilizando a variável cep
    let urlCEP = "https://brasilapi.com.br/api/cep/v1/" + cep;
    console.log("URL Generate: " + urlCEP);

    // executa o fetch com a url criada e via api traz os dados do cep inserido
    // .then(function(response){}): recebe o retorno o fetch e executa uma função
    fetch(urlCEP).then(function(response){
        // transforma o retorno do fetch response em json e exibe no console
        response.json().then(function(data){
            // Exibe os dados retornados no console para verificação
            console.log(data);
            
            // Preenchendo os campos automaticamente
            document.getElementById("endereco").value = data.street;
            document.getElementById("bairro").value = data.neighborhood;
            document.getElementById("cidade").value = data.city;
            document.getElementById("estado").value = data.state;
            
        })
        // tratativa de erros caso a api retorne erro
    }).catch(function(error){
        // Exibe o erro no console para verificação
        console.log("Error found: " + error);
    })
}

// Função para cadastrar o veículo
function cadastrarVeiculo(){
    // Pega os valores dos campos do formulário e armazena em variáveis
    let marca = document.getElementById("marca").value;
    let modelo = document.getElementById("modelo").value;
    let ano = document.getElementById("ano").value;
    let valor = document.getElementById("valor").value;
    let cep = document.getElementById("cep").value;
    let endereco = document.getElementById("endereco").value;
    let bairro = document.getElementById("bairro").value;
    let cidade = document.getElementById("cidade").value;
    let estado = document.getElementById("estado").value;
    let numero = document.getElementById("numero").value;
    let proprietario = '1';

     // Exibe os dados do cliente logado no console para verificação
    console.log("Cliente Logado:", cliente);

    // Pega o CPF do cliente logado e armazena na variável cpf_proprietario
    let cpf_proprietario = cliente.cpf;
 
    // Cria a url para o fetch utilizando as variáveis dos campos do formulário
    let urlCadastro = 'http://localhost:8002/gerenciar-bens/veiculos/adicionar-veiculo/?marca='
                    +encodeURIComponent(marca)
                    +'&modelo='+encodeURIComponent(modelo)
                    +'&ano='+encodeURIComponent(ano)
                    +'&valor='+encodeURIComponent(valor)
                    +'&cep='+encodeURIComponent(cep)
                    +'&endereco='+encodeURIComponent(endereco)
                    +'&bairro='+encodeURIComponent(bairro)
                    +'&cidade='+encodeURIComponent(cidade)
                    +'&estado='+encodeURIComponent(estado)
                    +'&numero='+encodeURIComponent(numero)
                    +'&proprietario='+encodeURIComponent(cpf_proprietario);

    // Exibe a URL gerada no console para verificação
    console.log("URL Generate: " + urlCadastro);

    // executa o fetch com a url criada e via api cadastra o veículo
    fetch(urlCadastro,{method: "POST"})
    .then(function(response){
        response.json().then(function(data){
            // Exibe os dados retornados no console para verificação
            console.log(data);
            
            // Verifica se a resposta contém um erro e exibe um alerta caso haja
            if (data.error || data.erro) {
                alert(data.error || data.erro);
                return;
            }

            // Exibe um alerta de sucesso e redireciona para a página de reserva de veículo
            alert("Cadastro bem-sucedido!");

            // Redireciona para a página de reserva de veículo
            window.location.href = "./reservaVeiculo.html";
        })
    })
    .catch(function(error){
        // Exibe o erro no console para verificação
        console.log("Error found: " + error);
    })
}