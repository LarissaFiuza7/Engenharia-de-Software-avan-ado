// Função para buscar o cliente com base no email e senha
function buscarCliente(){
    // Obter os valores do email e senha dos campos de entrada
    let email = document.getElementById("email").value;
    let senha = document.getElementById("senha").value;


    // Construir a URL para a requisição de login, incluindo os parâmetros de email e senha
    let urlLogin = 'http://localhost:8001/cliente/login/?email='+encodeURIComponent(email)+'&senha='+encodeURIComponent(senha);
    // Exibir a URL gerada no console para depuração
    console.log("URL Generate: " + urlLogin);

    // Realizar a requisição para o endpoint de login usando fetch
    fetch(urlLogin)
    .then(function(response){
        response.json().then(function(data){
            // Exibir os dados retornados no console para depuração
            console.log(data);
            // Verificar se a resposta contém um erro e exibir uma mensagem de alerta, caso contrário, proceder com o login
            if (data.error || data.erro) {
                alert(data.error || data.erro);
                return;
            }

            // Exibir uma mensagem de sucesso e armazenar os dados do cliente logado no localStorage, em seguida, redirecionar para a página de tipo de reserva
            alert("Login bem-sucedido!");
            // Armazenar os dados do cliente logado no localStorage para uso posterior
            localStorage.setItem("clienteLogado", JSON.stringify(data));
            // Exibir os dados do cliente logado no console para depuração
            console.log("Cliente Logado:", data);
            // Redirecionar para a página de tipo de reserva
            window.location.href = "./tipoReserva.html";
        })
    })
    .catch(function(error){
        // Exibir um alerta de erro caso a requisição falhe e registrar o erro no console para depuração
        console.log("Error found: " + error);
    })
}