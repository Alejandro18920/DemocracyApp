package com.gestionusuarios.ms_usuario.Repositorios;
import com.gestionusuarios.ms_usuario.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioUsuario extends MongoRepository<Usuario,String>{

    @Query("{'Email':?0}")
    public Usuario searchUserByEmail(String Email);

}
