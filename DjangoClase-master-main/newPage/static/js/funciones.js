function formatRut(input) {
  var rut = input.val().replace(/\D/g, '');
  rut = rut.substring(0, rut.length - 1) + '-' + rut.charAt(rut.length - 1);
  input.val(rut.replace(/(\d{1,3})(?=(\d{3})+(?:\.\d+)?$)/g, '$1.'));
}
$(document).ready(function () {
  $.ajax({
    url: "https://apis.digital.gob.cl/dpa/regiones",
    type: "GET",
    crossDomain: true,
    dataType: "jsonp",
    success: function (data) {
      $.each(data, function (i, item) {
        $("#cboRegiones").append(
          "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
        );
      });
    },
    error: function (xhr, status, error) {
      console.log("Error al obtener las regiones: " + error);
    },
  });
  
  $("#cboRegiones").change(function () {
    var idRegion = $("#cboRegiones").val();
    $("#cboProvincias").attr("disabled",false);
    $("#cboProvincias").empty();$("#cboProvincias").append("<option hidden disable>Seleccione una opcion</option>");
    $("#cboComunas").empty();
    $("#cboComunas").append("<option hidden disable>Seleccione una opcion</option>");$.ajax({
      url: "https://apis.digital.gob.cl/dpa/regiones/"+idRegion+"/provincias",
      type: "GET",
      crossDomain: true,
      dataType: "jsonp",
      success: function (data) {
        $.each(data, function (i, item) {
          $("#cboProvincias").append(
            "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
          );
        });
      },
      error: function (xhr, status, error) {
        console.log("Error al obtener las regiones: " + error);
      },
    });
  });
  $("#cboProvincias").change(function () {
    var idRegion = $("#cboRegiones").val();
    var idProvincia = $("#cboProvincias").val();
    $("#cboComunas").attr("disabled",false);
    $("#cboComunas").empty();
    $("#cboComunas").append("<option hidden disable>Seleccione una opcion</option>");
    $.ajax({
      url: "https://apis.digital.gob.cl/dpa/regiones/"+idRegion+"/provincias/"+idProvincia+"/comunas",
      type: "GET",
      crossDomain: true,
      dataType: "jsonp",
      success: function (data) {
        $.each(data, function (i, item) {
          $("#cboComunas").append(
            "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
          );
        });
      },
      error: function (xhr, status, error) {
        console.log("Error al obtener las regiones: " + error);
      },
    });
  });
});