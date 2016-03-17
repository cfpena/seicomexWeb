$(document).ready(function(){
  //controlador de menu principal deslizante
   $('.scrollspy').scrollSpy();
  //controlador de modales
  $('.modal-trigger').leanModal({
      dismissible: true, // Modal can be dismissed by clicking outside of the modal
      opacity: .8, // Opacity of modal background
      in_duration: 300, // Transition in duration
      out_duration: 200, // Transition out duration
    });
    //controlador de boton registro del modal registrarse
    $('#registro').click(function(){

      //condiciones de usuario valido en el formulario modal
      if(!$('#name').val()) Materialize.toast('El nombre está vacio', 4000);
      else if(!$('#lastname').val()) Materialize.toast('El apellido está vacio', 4000);
      else if(!$('#password').val()) Materialize.toast('La contraseña está vacia', 4000);
      else if($('#password').val()!=$('#password2').val()) Materialize.toast('Las contraseñas no coinciden', 4000);
      else if(!$('#email').val()) Materialize.toast('El email está vacio', 4000);
      else if($('#email').val()!=$('#email2').val()) Materialize.toast('Los email no coinciden', 4000);
      else {
      //llamada ajax al view registro del back-end

      $.ajax({
        url: "/registro",
        type: 'POST',
        data: {
            name:$('#name').val(),
            lastname:$('#lastname').val(),
            password:$('#password').val(),
            email:$('#email').val()

        }
        ,success: function(data,status) {
          Materialize.toast(data, 4000);
        }
    });
  }
    });

  $('#login').click(function(){
    $.ajax({
      url: "/login",
      type: 'POST',
      data: {
          password:$('#passwordLogin').val(),
          email:$('#emailLogin').val()

      }
      ,success: function(data,status) {
        if (data=='true') window.location = "/tramites";
        else Materialize.toast(data, 4000);
      }
  });
  })
 });
