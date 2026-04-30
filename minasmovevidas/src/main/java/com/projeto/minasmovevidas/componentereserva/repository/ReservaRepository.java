package com.projeto.minasmovevidas.componentereserva.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import com.projeto.minasmovevidas.componentereserva.model.Reserva;

public interface ReservaRepository extends MongoRepository<Reserva, String> {
}