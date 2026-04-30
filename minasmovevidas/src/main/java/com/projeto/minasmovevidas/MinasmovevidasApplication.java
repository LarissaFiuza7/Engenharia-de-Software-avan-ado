package com.projeto.minasmovevidas;

import com.mongodb.MongoClientSettings;
import com.projeto.minasmovevidas.componentebens.service.BensComponentImpl;
import com.projeto.minasmovevidas.shared.IBensComponent;
import com.projeto.minasmovevidas.shared.IReservaComponent;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.projeto.minasmovevidas.componenteclientes.model.Cliente;
import com.projeto.minasmovevidas.componentebens.model.Bens;
import com.projeto.minasmovevidas.shared.IClienteComponent;

import java.time.LocalDate;


@SpringBootApplication
public class MinasmovevidasApplication implements CommandLineRunner {

	@Autowired
	private IClienteComponent clienteComponent;
    @Autowired
    private MongoClientSettings mongoClientSettings;
	@Autowired
	private IBensComponent bensComponent;
	@Autowired
	private IReservaComponent reservaComponent;


	public static void main(String[] args) {
		SpringApplication.run(MinasmovevidasApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {

		System.out.println("Iniciando teste de componente Cliente...");

		// Criando cliente
		Cliente cliente = new Cliente();
		cliente.setNomeCompleto("Insira o nome do Cliente");
		cliente.setCpf("Insira o CPF do cliente");
		cliente.setEmail("Insira o email do cliente");
		cliente.setSenha("Insira a senha do cliente");

		// Salvando no Mongo
		clienteComponent.salvar(cliente);

		System.out.println("Cliente salvo!");

		// Buscando do Mongo
		Cliente buscado = clienteComponent.buscarPorEmail("Insira o email do cliente");

		if (buscado != null) {
			System.out.println("Cliente encontrado: " + buscado.getNomeCompleto());
		} else {
			System.out.println("Cliente não encontrado.");
		}

		Bens bem = new Bens();
		bem.setNome("Nome do bem");
		bem.setDescricao("Descrição do bem");
		bem.setEndereco("Endereço do bem");
		bem.setNumero("numero do bem (se tiver)");
		bem.setCep("CEP do bem");

		bensComponent.cadastrar(bem,"CPF do proprietario do bem");

		System.out.println("Bem Cadastrado com Sucesso");

		reservaComponent.criarReserva(
				"CPF do cliente que esta alugando", // CPF do cliente já cadastrado
				"ID do bem", // pega do banco
				LocalDate.now(),
				LocalDate.now().plusDays(5)
		);

		System.out.println("Reserva criada com sucesso!");
	}
}