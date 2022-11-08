package com.gestionusuarios.ms_usuario.Repositorios;

import com.gestionusuarios.ms_usuario.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermiso  extends MongoRepository<Permiso,String> {
}
