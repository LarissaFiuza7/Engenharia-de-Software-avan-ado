package com.projeto.minasmovevidas.shared;

import java.util.List;
import com.projeto.minasmovevidas.componentebens.model.Bens;

public interface IBensComponent {

    Bens cadastrar(Bens bem, String cpfCliente);

    Bens buscarPorId(String id);

    List<Bens> listarTodos();
}