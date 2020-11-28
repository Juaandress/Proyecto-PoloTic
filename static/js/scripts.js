$(document).ready(function() {
    //calendar
    $("#calendario").datepicker({
      dateFormat: "dd-mm-yy",
  
      minDate: 0, //calendar starts from today
      maxDate: "8m", //calendar ends in 12 months
  
      beforeShowDay: function(date) {
        let day = date.getDay(), //days from 0 to 6
          year = date.getUTCFullYear(),
          month = date.getUTCMonth() + 1, //months from 1-12
          dayNumber = date.getUTCDate();
  
        //disable hollidays in 2018     --feriados argentinos 2018
        if (year === 2018) {
          if (
            (month === 1 && dayNumber === 1) || //año nuevo
            (month === 2 && (dayNumber === 12 || dayNumber === 13)) || //carnaval
            (month === 3 && dayNumber === 24) || //día de la memoria
            (month === 3 && dayNumber === 30) || //viernes santo
            (month === 4 && dayNumber === 2) || //veteranos malvinas
            (month === 5 && dayNumber === 1) || //trabajador
            (month === 5 && dayNumber === 25) || //revolución de mayo
            (month === 6 && (dayNumber === 17 || dayNumber === 20)) || //fallecimiento de guemes | bandera
            (month === 7 && dayNumber === 9) || //independencia
            (month === 8 && dayNumber === 20) || //fallecimiento de san martin
            (month === 10 && dayNumber === 15) || //diversidad cultural
            (month === 11 && dayNumber === 19) || //soberanía nacional
            (month === 12 && (dayNumber === 8 || dayNumber === 25)) //inmaculada concepción | navidad
          ) {
            return [false];
          }
        }
  
        if (day === 0 || day === 6)
          return [false]; //disable weekends
        else return [true];
      },
  
      //spanish
      dayNamesMin: ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa"],
      monthNames: [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
      ]
    });
  
    //confirmation (modal when submit)
    $("form").submit(function(e) {
      e.preventDefault();
  
      //set inputs in values
      let dni = $("#dni").val(),
        tel = $("#tel").val(),
        email = $("#email").val(),
        apellido = $("#apellido").val(),
        nombre = $("#nombre").val(),
        sexo = $("input:checked").val(),
        fecha = $("#calendario").val(),
        horario = $("#horario").val(),
        motivo = "",
        comentarios = $("#comentarios").val();
  
      if ($("#alcoholismo").is(":checked")) motivo = motivo + " Alcoholismo.";
      if ($("#drogadiccion").is(":checked")) motivo = motivo + " Drogadicción.";
      if ($("#crisis").is(":checked")) motivo = motivo + " Crisis existencial.";
      if ($("#otra").is(":checked")) motivo = motivo + " Otra patología.";
  
      //insert values in modal
      $(".modalApellidoYNombre").text(apellido + ", " + nombre);
      $(".modalDNI").text(dni);
      $(".modalEmail").text(email);
      $(".modalFecha").text(fecha);
      $(".modalHorario").text(horario);
      $(".modalMotivo").text(motivo);
  
      $("#modalConfirmar").show("slow");
  
      //buttons
      $("#cancelar").click(function(e) {
        e.preventDefault();
        $("#modalConfirmar").hide("slow");
      });
  
      $("#confirmar").click(function(e) {
        e.preventDefault();
        $("#modalConfirmar").hide("slow");
  
        //generate random ID
        let randomID = parseInt(Math.random() * 800000 + 100000);
        //insert value in html
        $("#idTurno").text(randomID);
  
        $("#modalTurnoID").show("slow");
  
        $("#cerrarTurnoID").click(function() {
          //reset values
          $("#dni").val("");
          $("#tel").val("");
          $("#email").val("");
          $("#apellido").val(""),
            $("#nombre").val(""),
            $("input:checked").val(""),
            $("#calendario").val(""),
            $("#horario").val(""),
            (motivo = "");
          $("#comentarios").val("");
  
          $("#modalTurnoID").hide("slow");
        });
      });
    });
  });