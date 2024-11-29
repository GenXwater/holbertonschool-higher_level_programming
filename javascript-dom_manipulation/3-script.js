document.getElementById('toggle_header').addEventListener('click', function() {
  const header = document.getElementsByClassName('green')[0] || document.getElementsByClassName('red')[0];
  if (header.classList.contains('green')) {
      header.classList.remove('green');
      header.classList.add('red');
  } else {
      header.classList.remove('red');
      header.classList.add('green');
  }
});
