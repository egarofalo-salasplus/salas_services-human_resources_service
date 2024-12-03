function sendImputation(board_id, item_id, column_id, previous_value, value) {
    const token = window.salasApiKey;
    let sum = Number(previous_value) + Number(value)
    let result = sum.toString();
    fetch(`${window.mondayBaseUrl}/set-column-value`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ${token}}'
        },
        body: JSON.stringify({
            board_id: board_id,
            item_id: item_id,
            column_id: column_id,
            value: result
        }),
        credentials: "include",
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Horas enviadas correctamente para el ítem ID: ' + data.item_id);
            } else {
                alert('Error: ' + data.message);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Hubo un problema al enviar las horas.');
        });
}
