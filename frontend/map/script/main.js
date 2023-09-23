// Перевіряємо наявність та значення access token в localStorage
const accessToken = localStorage.getItem('access_token');
const mapType = accessToken && accessToken.trim() !== '' ? 'authorized' : 'default';

// Формуємо параметри запиту залежно від значення access token
const queryParams = {
  status: 200,
  map: mapType
};

// Відправляємо GET запит з відповідними параметрами
fetch('/api/data?' + new URLSearchParams(queryParams))
  .then(response => response.json())
  .then(data => {
    if (data.status === 200 && Array.isArray(data.coordinates)) {
      handleCoordinates(data.coordinates);
    }
  })
  .catch(error => console.error('Помилка запиту: ', error));

function handleCoordinates(coordinates) {
  const script = document.createElement('script');
  script.src = 'path/to/other-file.js';
  document.body.appendChild(script);

  script.onload = function() {
    window.heat_point = coordinates;
  }
}
