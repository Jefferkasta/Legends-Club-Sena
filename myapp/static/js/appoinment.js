// Obtener elementos HTML
const calendarBody = document.getElementById('calendar-body');

// Función para crear el calendario
function crearCalendario() {
    // Obtener fecha actual
    const fecha = new Date();

    const monthText = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
      ];

    // Establecer el primer día del mes y el último día del mes
    const primerDia = new Date(fecha.getFullYear(), fecha.getMonth(), 1);
    const ultimoDia = new Date(fecha.getFullYear(), fecha.getMonth() + 1, 0);
    console.log(monthText[fecha.getMonth()]);
    // Limpiar el cuerpo del calendario
    calendarBody.innerHTML = '';

    let date = 1;
    // Crear filas para el calendario
    for (let i = 0; i < 6; i++) {
        const row = document.createElement('tr');

        // Crear columnas para los días de la semana
        for (let j = 0; j < 7; j++) {
            const cell = document.createElement('td');

            // Llenar celdas con números de días
            if (i === 0 && j < primerDia.getDay()) {
                const cellText = document.createTextNode('');
                cell.appendChild(cellText);
            } else if (date > ultimoDia.getDate()) {
                break;
            } else {
                const cellText = document.createTextNode(date);
                cell.appendChild(cellText);
                date++;
            }

            row.appendChild(cell);
        }

        calendarBody.appendChild(row);
    }
}

// Llamar a la función para crear el calendario al cargar la página
window.onload = crearCalendario;