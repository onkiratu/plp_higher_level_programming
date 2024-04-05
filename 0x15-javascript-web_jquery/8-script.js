$.ajax({
	method: "GET",
	url: "https://swapi-api.alx-tools.com/api/films/?format=json",
	datatype: "json",
	success: function(data) {
	  let movieTitles = data.results.map(function (movie) {
		return movie.title;
	  })
	  let movieList = $("UL#list_movies");
	  $.each(movieTitles, function(index, title) {
	    let listMovie = $("<li>" + title + "</li>");
	    movieList.append(listMovie);
	})
	}
});
