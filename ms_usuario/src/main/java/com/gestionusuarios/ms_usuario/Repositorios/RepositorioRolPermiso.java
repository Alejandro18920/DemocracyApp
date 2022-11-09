package com.gestionusuarios.ms_usuario.Repositorios;

import com.gestionusuarios.ms_usuario.Modelos.RolPermiso;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRolPermiso extends MongoRepository<RolPermiso,String> {
}
