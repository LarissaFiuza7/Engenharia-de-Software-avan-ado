// Verificar se o cliente está logado
const cliente = JSON.parse(localStorage.getItem("clienteLogado"));

// Se não houver cliente logado, redirecionar para a página de login
console.log("Cliente Logado:", cliente);
if (!cliente) {
    alert("Você precisa estar logado para acessar esta página.");
    window.location.href = "./login.html";
}

function buscarCep(){
    let cep = document.getElementById("cep").value;

    let urlCEP = "https://brasilapi.com.br/api/cep/v1/" + cep;
    console.log("URL Generate: " + urlCEP);

    // executa o fetch com a url criada e via api traz os dados do cep inserido
    // .then(function(response){}): recebe o retorno o fetch e executa uma função
    fetch(urlCEP).then(function(response){
        // transforma o retorno do fetch response em json e exibe no console
        response.json().then(function(data){
            console.log(data);
            
            // Preenchendo os campos automaticamente
            document.getElementById("endereco").value = data.street;
            document.getElementById("bairro").value = data.neighborhood;
            document.getElementById("cidade").value = data.city;
            document.getElementById("estado").value = data.state;
            
        })
        // tratativa de erros caso a api retorne erro
    }).catch(function(error){
        console.log("Error found: " + error);
    })
}

function cadastrarImovel(){
    // Captura os valores dos campos do formulário
    let cep = document.getElementById("cep").value;
    let endereco = document.getElementById("endereco").value;
    let bairro = document.getElementById("bairro").value;
    let cidade = document.getElementById("cidade").value;
    let estado = document.getElementById("estado").value;
    let numero = document.getElementById("numero").value;
    let complemento = document.getElementById("complemento").value;
    let qtde_comodos = document.getElementById("comodos").value;
    let metros_quadrados = document.getElementById("metros_quadrados").value;
    let valor = document.getElementById("valor").value;
    let proprietario = '1';

    // Exibe os valores capturados no console para verificação
    console.log("Cliente Logado:", cliente);

    // O CPF do proprietário é obtido a partir do cliente logado
    let cpf_proprietario = cliente.cpf;
    
    // Monta a URL para o cadastro do imóvel, incluindo os parâmetros necessários
    let urlCadastro = 'http://localhost:8002/gerenciar-bens/imoveis/adicionar-imovel/?cep='
                    +encodeURIComponent(cep)
                    +'&endereco='+encodeURIComponent(endereco)
                    +'&bairro='+encodeURIComponent(bairro)
                    +'&cidade='+encodeURIComponent(cidade)
                    +'&estado='+encodeURIComponent(estado)
                    +'&numero='+encodeURIComponent(numero)
                    +'&complemento='+encodeURIComponent(complemento)
                    +'&qtde_comodos='+encodeURIComponent(qtde_comodos)
                    +'&metros_quadrados='+encodeURIComponent(metros_quadrados)
                    +'&valor='+encodeURIComponent(valor)
                    +'&proprietario='+encodeURIComponent(cpf_proprietario);

    // Exibe a URL gerada no console para verificação
    console.log("URL Generate: " + urlCadastro);

    // Executa o fetch para cadastrar o imóvel, utilizando o método POST
    fetch(urlCadastro,{method: "POST"})
    .then(function(response){
        response.json().then(function(data){
            // Exibe a resposta da API no console para verificação
            console.log(data);
            
            // Verifica se a resposta contém um erro e exibe uma mensagem de alerta caso haja, caso contrário, exibe uma mensagem de sucesso e redireciona para a página de reservas
            if (data.error || data.erro) {
                alert(data.error || data.erro);
                return;
            }

            // Se o cadastro for bem-sucedido, exibe uma mensagem de sucesso e redireciona para a página de reservas
            alert("Cadastro bem-sucedido!");
 
            // Redireciona para a página de reservas
            window.location.href = "./reserva.html";
        })
    })
    .catch(function(error){
        // Exibe qualquer erro encontrado durante o processo de cadastro no console para depuração
        console.log("Error found: " + error);
    })
}