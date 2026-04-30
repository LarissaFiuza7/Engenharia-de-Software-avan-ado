package com.projeto.minasmovevidas.componenteclientes.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import com.projeto.minasmovevidas.componenteclientes.model.Cliente;

public interface ClienteRepository extends MongoRepository<Cliente, String> {

    Cliente findByEmail(String email);
    Cliente findByCpf(String cpf);
}