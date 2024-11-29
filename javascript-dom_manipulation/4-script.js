document.getElementById('add_item').addEventListener('click', function () {
  const newElement = document.createElement('li'); // Crée new élement.
  newElement.textContent = 'Item'; // Défifnit le texte dans notre élément <li>
  document.querySelector('ul.my_list').appendChild(newItem); // Ajoute l'ément a la liste <ul>
});
