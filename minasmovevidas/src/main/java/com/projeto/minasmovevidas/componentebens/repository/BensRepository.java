package com.projeto.minasmovevidas.componentebens.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import com.projeto.minasmovevidas.componentebens.model.Bens;

public interface BensRepository extends MongoRepository<Bens, String> {

}