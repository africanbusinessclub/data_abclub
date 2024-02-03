// script.js
$(document).ready(function () {
  var table = $("#tableResultats").DataTable();

  $("#selectContinent").on("change", function () {
    var selectedContinent = $(this).val();
    table.columns(1).search(selectedContinent).draw();
  });
});
