package com.gestionusuarios.ms_usuario.Repositorios;
import com.gestionusuarios.ms_usuario.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioUsuario extends MongoRepository<Usuario,String>{
}
