package com.gestionusuarios.ms_usuario.Controladores;

import com.gestionusuarios.ms_usuario.Modelos.Rol;
import com.gestionusuarios.ms_usuario.Repositorios.RepositorioRol;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/rol")
public class ControladorRol {
    @Autowired
    private RepositorioRol _repo_rol;

    @PostMapping("/crear")
    public Rol crearRol(@RequestBody Rol rolEntrada){
        return _repo_rol.save(rolEntrada);
    }

    @GetMapping("")
    public List<Rol> listarRol(){
        return _repo_rol.findAll();
    }

    @DeleteMapping("/eliminar/{_id_rol}")
    public String eliminarRol(@PathVariable String _id_rol) {
        _repo_rol.deleteById(_id_rol);
        return"El usuario con código " + _id_rol + " ha sido eliminado";
    }

    @PutMapping("/actualizar/{_id_rol}")
    public String actualizarRol(@PathVariable String _id_rol, @RequestBody Rol rolEntrada) {
        Rol rolConsulta = _repo_rol.findById(_id_rol).orElse(null);
        rolConsulta.setNombre(rolEntrada.getNombre());
        rolConsulta.setDescripcion(rolEntrada.getDescripcion());
        _repo_rol.save(rolConsulta);
        return "El usuario con código " + _id_rol + " ha sido actualizado";
    }
}
