package com.projeto.minasmovevidas.componenteclientes.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.projeto.minasmovevidas.componenteclientes.model.Cliente;
import com.projeto.minasmovevidas.componenteclientes.repository.ClienteRepository;
import com.projeto.minasmovevidas.shared.IClienteComponent;

@Component
public class ClienteComponentImpl implements IClienteComponent {

    @Autowired
    private ClienteRepository repository;

    @Override
    public Cliente salvar(Cliente cliente) {
        return repository.save(cliente);
    }

    @Override
    public Cliente buscarPorEmail(String email) {
        return repository.findByEmail(email);
    }
    @Override
    public Cliente buscarPorCpf(String cpf) {
        return repository.findByCpf(cpf);
    }
}