package com.gestionusuarios.ms_usuario.Repositorios;

import com.gestionusuarios.ms_usuario.Modelos.RolPermiso;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
public interface RepositorioRolPermiso extends MongoRepository<RolPermiso,String> {
    @Query("{'rol.$id': ObjectId(?0),'permiso.$id': ObjectId(?1)}")
    public RolPermiso consultarRolPermiso(String _id_rol, String _id_permiso);
}
