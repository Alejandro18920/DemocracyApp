package com.gestionusuarios.ms_usuario.Controladores;

import com.gestionusuarios.ms_usuario.Modelos.Rol;
import com.gestionusuarios.ms_usuario.Modelos.Usuario;
import com.gestionusuarios.ms_usuario.Repositorios.RepositorioRol;
import com.gestionusuarios.ms_usuario.Repositorios.RepositorioUsuario;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;


@RestController
@RequestMapping("/usuarios")
public class ControladorUsuario {

    @Autowired
    private RepositorioUsuario _repo_usuario;
    @Autowired
    private RepositorioRol _repo_rol;

    @PostMapping ("/crear")
    public Usuario crearUsuario(@RequestBody Usuario usuarioEntrada){
        usuarioEntrada.setPassword(convertirSHA256(usuarioEntrada.getPassword()));
        return _repo_usuario.save(usuarioEntrada);
    }

    @GetMapping("")
    public List<Usuario> listarUsuario(){
        return _repo_usuario.findAll();
    }

    @DeleteMapping("/eliminar/{_id_usuario}")
    public String eliminarUsuario(@PathVariable String _id_usuario) {
        _repo_usuario.deleteById(_id_usuario);
        return"El usuario con código " + _id_usuario + " ha sido eliminado";
    }

    @PutMapping("/actualizar/{_id_usuario}")
    public String actualizarUsuario(@PathVariable String _id_usuario, @RequestBody Usuario usuarioEntrada) {
        Usuario usuarioConsulta= _repo_usuario.findById(_id_usuario).orElse(null);
        usuarioConsulta.setEmail(usuarioEntrada.getEmail());
        usuarioConsulta.setUsername(usuarioEntrada.getUsername());
        usuarioConsulta.setPassword(convertirSHA256(usuarioEntrada.getPassword()));
        _repo_usuario.save(usuarioConsulta);
        return"El usuario con código " + _id_usuario + " ha sido actualizado";
    }

    @PutMapping("/asignar/{_id_usuario}/rol/{_id_rol}")
    public String asignarRol(@PathVariable String _id_usuario, @PathVariable String _id_rol) {
        Usuario usuarioConsulta= _repo_usuario.findById(_id_usuario).orElse(null);
        Rol rolConsulta= _repo_rol.findById(_id_rol).orElse(null);
        usuarioConsulta.setRol(rolConsulta);
        _repo_usuario.save(usuarioConsulta);
        return"El usuario con código " + _id_usuario + " ha sido actualizado";
    }
    public String convertirSHA256(String password) {
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(password.getBytes());
        StringBuffer sb = new StringBuffer();
        for (byte b : hash) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }


}
