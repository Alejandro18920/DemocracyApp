package com.gestionusuarios.ms_usuario.Modelos;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document
public class RolPermiso {
    @Id
    String _id;
    @DBRef
    Rol rol;
    @DBRef
    Permiso permiso;

    public RolPermiso(Rol rol, Permiso permiso) {
        this.rol = rol;
        this.permiso = permiso;
    }

    public Rol getRol() {
        return rol;
    }

    public void setRol(Rol rol) {
        this.rol = rol;
    }

    public Permiso getPermiso() {
        return permiso;
    }

    public void setPermiso(Permiso permiso) {
        this.permiso = permiso;
    }
}
