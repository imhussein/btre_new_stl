function onImageClick(list_id) {
  window.location.href = `/listings/${list_id}`;
}

$(".alert").alert();

setTimeout(() => {
  $("#message").fadeOut("slow");
}, 3000);
