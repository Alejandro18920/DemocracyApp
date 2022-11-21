package com.gestionusuarios.ms_usuario.Controladores;

import com.gestionusuarios.ms_usuario.Modelos.Permiso;
import com.gestionusuarios.ms_usuario.Modelos.Rol;
import com.gestionusuarios.ms_usuario.Modelos.RolPermiso;
import com.gestionusuarios.ms_usuario.Repositorios.RepositorioPermiso;
import com.gestionusuarios.ms_usuario.Repositorios.RepositorioRol;
import com.gestionusuarios.ms_usuario.Repositorios.RepositorioRolPermiso;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;


@RequestMapping("/rolpermiso")
@RestController


public class ControladorRolPermiso {

    @Autowired
    RepositorioRolPermiso _repo_RolPermiso;
    @Autowired
    RepositorioRol _repo_Rol;
    @Autowired
    RepositorioPermiso _repo_Permiso;

    @GetMapping("")
    public List<RolPermiso> listarRolPermiso(){
        return _repo_RolPermiso.findAll();

    }

    @PostMapping("/crear/{_id_rol}/{_id_permiso}")
    public RolPermiso crearRolPermiso(@PathVariable String _id_rol, @PathVariable String _id_permiso){

        Rol rolconsulta= _repo_Rol.findById(_id_rol).orElse(null);
        Permiso permisoconsulta= _repo_Permiso.findById(_id_permiso).orElse(null);
        RolPermiso rolPermiso = new RolPermiso(rolconsulta,permisoconsulta);
        return _repo_RolPermiso.save(rolPermiso);

    }

    @DeleteMapping("/eliminar/{_id_RolPermiso}")
    public String eliminarRolPermiso(@PathVariable String _id_RolPermiso){
        _repo_RolPermiso.deleteById(_id_RolPermiso);
        return "El RolPermiso con identificador " + _id_RolPermiso + " ha sido eliminado";
    }

    @PutMapping("/{_id_RolPermiso}/{_id_rol}/{_id_permiso}")
    public String actualizarRolPermiso(@PathVariable String _id_rol,
                                           @PathVariable String _id_permiso,
                                           @PathVariable String _id_RolPermiso){
        RolPermiso rolpermisoconsulta= _repo_RolPermiso.findById(_id_RolPermiso).orElse(null);
        Rol rolconsulta= _repo_Rol.findById(_id_rol).orElse(null);
        Permiso permisoconsulta= _repo_Permiso.findById(_id_permiso).orElse(null);
        rolpermisoconsulta.setRol(rolconsulta);
        rolpermisoconsulta.setPermiso(permisoconsulta);
        _repo_RolPermiso.save(rolpermisoconsulta);
        return "se ha actualizado el permiso del rol";

    }

    @PostMapping("/{_id_rol}")
    public RolPermiso obtenerPermiso(@PathVariable String _id_rol,
                                     @RequestBody Permiso permisoEntrada,
                                     HttpServletResponse respuesta) throws IOException {
        Permiso permisoConsulta = _repo_Permiso.consultarPermiso(permisoEntrada.getUrl(),
                permisoEntrada.getMetodo());

        if (permisoConsulta != null) {
            return _repo_RolPermiso.consultarRolPermiso(_id_rol,
                    permisoConsulta.get_id());
        } else {
            respuesta.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }
    }
}
