function criarCliente(){
    // captura os valores dos campos do formulário
    let nome_completo = document.getElementById("nome_completo").value;
    let email = document.getElementById("email").value;
    let senha = document.getElementById("senha").value;
    let cpf = document.getElementById("cpf").value;
    let telefone = document.getElementById("numero_telefone").value;
    let data_nascimento = document.getElementById("data_nascimento").value;

    // cria url de cadastro com os parâmetros do formulário
    let urlCadastro = 'http://localhost:8001/cliente/cadastrar-cliente/?nome='+encodeURIComponent(nome_completo)
                    +'&cpf='+encodeURIComponent(cpf)
                    +'&email='+encodeURIComponent(email)
                    +'&senha='+encodeURIComponent(senha)
                    +'&data_nascimento='+encodeURIComponent(data_nascimento)
                    +'&numero_telefone='+encodeURIComponent(telefone);
    // exibe a url gerada no console para verificação
    console.log("URL Generate: " + urlCadastro);

    // realiza a requisição POST para o backend usando a URL gerada
    fetch(urlCadastro,{method: "POST"})
    .then(function(response){
        response.json().then(function(data){
            // exibe a resposta do backend no console para verificação
            console.log(data);
            // verifica se a resposta contém um erro e exibe uma mensagem de alerta, caso contrário, exibe uma mensagem de sucesso e redireciona para a página de login
            if (data.error || data.erro) {
                alert(data.error || data.erro);
                return;
            }
            // exibe uma mensagem de sucesso e redireciona para a página de login
            alert("Cadastro bem-sucedido!");
            // redireciona para a página de login
            window.location.href = "./login.html";
        })
    })
    .catch(function(error){
        // exibe o erro no console para depuração
        console.log("Error found: " + error);
    })
}