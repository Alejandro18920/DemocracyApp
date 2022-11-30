package com.gestionusuarios.ms_usuario.Controladores;


import com.gestionusuarios.ms_usuario.Modelos.Permiso;
import com.gestionusuarios.ms_usuario.Modelos.Rol;
import com.gestionusuarios.ms_usuario.Repositorios.RepositorioPermiso;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;
@CrossOrigin
@RestController
@RequestMapping("/permisos")
public class ControladorPermiso {
    @Autowired
    private RepositorioPermiso _repo_permiso;

    @PostMapping("/crear")
    public Permiso crearPermiso(@RequestBody Permiso permisoEntrada){
        return this._repo_permiso.save(permisoEntrada);
    }

    @GetMapping("")
    public List<Permiso> listarPermiso(){
        return this._repo_permiso.findAll();
    }



    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("/eliminar/{_id_permiso}")
    public void eliminarPermiso(@PathVariable String _id_permiso){
        Permiso permisoConsulta=this._repo_permiso.findById(_id_permiso)
                .orElse(null);
        if(permisoConsulta!=null){
            this._repo_permiso.deleteById(_id_permiso);
        }
    }

    @PutMapping("/actualizar/{_id_permiso}")
    public String actualizarPermiso(@PathVariable String _id_permiso, @RequestBody Permiso permisoEntrada) {
        Permiso permisoConsulta = _repo_permiso.findById(_id_permiso).orElse(null);
        permisoConsulta.setUrl(permisoEntrada.getUrl());
        permisoConsulta.setMetodo(permisoEntrada.getMetodo());
        _repo_permiso.save(permisoConsulta);
        return "El usuario con código " + _id_permiso + " ha sido actualizado";
    }
}
