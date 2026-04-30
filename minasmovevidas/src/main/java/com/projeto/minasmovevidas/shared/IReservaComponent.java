package com.projeto.minasmovevidas.shared;

import java.time.LocalDate;
import java.util.List;
import com.projeto.minasmovevidas.componentereserva.model.Reserva;

public interface IReservaComponent {

    Reserva criarReserva(String cpfCliente, String idBem, LocalDate dataInicio, LocalDate dataFim);

    Reserva buscarPorId(String id);

    List<Reserva> listarTodas();
}