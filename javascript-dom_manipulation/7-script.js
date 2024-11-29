fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json()) // Parse la response as JSON
.then(data => {
  const movies = data.results; // Extraire un array de movies
  const list = document.getElementById('list_movies'); // Get the <ul> element with id="list_movies"

  movies.forEach(movie => {
    const listItem = document.createElement('li'); // Create a new <li> element
    listItem.textContent = movie.title; // Set the text content to the movie's title
    list.appendChild(listItem); // Append the <li> to the <ul>
  });
})
