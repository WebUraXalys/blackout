// Відправляє GET запит з параметрами status: 200 та map: default при завантаженні сторінки
fetch('/api/data?status=200&map=default')
  .then(response => response.json())
  .then(data => {
    // Якщо відповідь містить статус 200 та масив координат, то запускаємо функцію для обробки цих даних
    if (data.status === 200 && Array.isArray(data.coordinates)) {
      handleCoordinates(data.coordinates);
    }
  })
  .catch(error => console.error('Помилка запиту: ', error));

function handleCoordinates(coordinates) {
  // Підключаємо інший js файл, в якому буде використовуватися масив з координатами
  const script = document.createElement('script');
  script.src = 'path/to/other-file.js';
  document.body.appendChild(script);

  // Записуємо масив координат у змінну heat_point у іншому js файлі
  script.onload = function() {
    window.heat_point = coordinates;
  }
}
