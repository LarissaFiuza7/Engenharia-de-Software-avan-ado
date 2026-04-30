package com.projeto.minasmovevidas.componentereserva.service;

import java.time.LocalDate;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.projeto.minasmovevidas.componentebens.model.Bens;
import com.projeto.minasmovevidas.componenteclientes.model.Cliente;
import com.projeto.minasmovevidas.componentereserva.model.Reserva;
import com.projeto.minasmovevidas.componentereserva.repository.ReservaRepository;
import com.projeto.minasmovevidas.shared.IBensComponent;
import com.projeto.minasmovevidas.shared.IClienteComponent;
import com.projeto.minasmovevidas.shared.IReservaComponent;

@Component
public class ReservaComponentImpl implements IReservaComponent {

    @Autowired
    private ReservaRepository repository;

    @Autowired
    private IClienteComponent clienteComponent;

    @Autowired
    private IBensComponent bensComponent;

    @Override
    public Reserva criarReserva(String cpfCliente, String idBem, LocalDate dataInicio, LocalDate dataFim) {

        // valida cliente
        Cliente cliente = clienteComponent.buscarPorCpf(cpfCliente);
        if (cliente == null) {
            throw new RuntimeException("Cliente não encontrado");
        }

        // valida bem
        Bens bem = bensComponent.buscarPorId(idBem);
        if (bem == null) {
            throw new RuntimeException("Bem não encontrado");
        }

        // valida regra de negócio
        if (dataFim.isBefore(dataInicio)) {
            throw new RuntimeException("Data fim não pode ser antes da data início");
        }

        // cria reserva
        Reserva reserva = new Reserva();
        reserva.setCpfCliente(cpfCliente);
        reserva.setIdBem(idBem);
        reserva.setDataInicio(dataInicio);
        reserva.setDataFim(dataFim);

        return repository.save(reserva);
    }

    @Override
    public Reserva buscarPorId(String id) {
        return repository.findById(id).orElse(null);
    }

    @Override
    public List<Reserva> listarTodas() {
        return repository.findAll();
    }
}