$.ajax({
  method: "GET',
  url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
  datatype: "json",
  success: function (data) {
    let translation = data.hello;
	$("DIV#hello").text(translation);
  }
});
