package com.gestionusuarios.ms_usuario.Repositorios;

import com.gestionusuarios.ms_usuario.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRol extends MongoRepository<Rol,String> {
}
