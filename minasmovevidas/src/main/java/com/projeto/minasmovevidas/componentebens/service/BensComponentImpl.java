package com.projeto.minasmovevidas.componentebens.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.projeto.minasmovevidas.componentebens.model.Bens;
import com.projeto.minasmovevidas.componentebens.repository.BensRepository;
import com.projeto.minasmovevidas.componenteclientes.model.Cliente;
import com.projeto.minasmovevidas.shared.IBensComponent;
import com.projeto.minasmovevidas.shared.IClienteComponent;

@Component
public class BensComponentImpl implements IBensComponent {

    @Autowired
    private BensRepository repository;

    @Autowired
    private IClienteComponent clienteComponent; // consumo via interface

    @Override
    public Bens cadastrar(Bens bem, String cpfCliente) {

        // busca cliente via interface
        Cliente cliente = clienteComponent.buscarPorCpf(cpfCliente);

        if (cliente == null) {
            throw new RuntimeException("Cliente não encontrado para o CPF informado");
        }

        // vincula o bem ao cliente
        bem.setCpfCliente(cpfCliente);

        return repository.save(bem);
    }

    @Override
    public Bens buscarPorId(String id) {
        return repository.findById(id).orElse(null);
    }

    @Override
    public List<Bens> listarTodos() {
        return repository.findAll();
    }
}