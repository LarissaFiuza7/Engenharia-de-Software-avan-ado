package com.projeto.minasmovevidas.shared;

import com.projeto.minasmovevidas.componenteclientes.model.Cliente;

public interface IClienteComponent {

    Cliente salvar(Cliente cliente);

    Cliente buscarPorEmail(String email);

    Cliente buscarPorCpf(String cpf);
}