package com.gestionusuarios.ms_usuario.Controladores;

import com.gestionusuarios.ms_usuario.Modelos.Permiso;
import com.gestionusuarios.ms_usuario.Modelos.Rol;
import com.gestionusuarios.ms_usuario.Modelos.Usuario;
import com.gestionusuarios.ms_usuario.Repositorios.RepositorioRol;
import com.gestionusuarios.ms_usuario.Repositorios.RepositorioUsuario;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

@CrossOrigin
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

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("/eliminar/{_id_usuario}")
    public void eliminarUsuario(@PathVariable String _id_usuario){
        Usuario usuarioConsulta=this._repo_usuario.findById(_id_usuario)
                .orElse(null);
        if(usuarioConsulta!=null){
            this._repo_usuario.deleteById(_id_usuario);
        }
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

    @PostMapping("/login")
    public Usuario iniciarSesion(@RequestBody Usuario usuarioEntrada,
                                 HttpServletResponse codigoRespuestaHttp) throws IOException {
        String Email = usuarioEntrada.getEmail();
        Usuario usuarioConsulta = _repo_usuario.searchUserByEmail(Email);
        if (usuarioConsulta != null && usuarioConsulta.getPassword().equals(convertirSHA256(usuarioEntrada.getPassword()))) {
            System.out.println("inicio de sesion exitoso");
            usuarioConsulta.setPassword("");
            return usuarioConsulta;
        } else {
            System.out.println("datos incorrectos " + Email + " " +usuarioEntrada);
            codigoRespuestaHttp.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }
    }

}
