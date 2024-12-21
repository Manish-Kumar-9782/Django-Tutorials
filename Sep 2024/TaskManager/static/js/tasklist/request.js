// Async function to checkItem
async function fetchRequest(url, data, resFunc) {
    const csrftoken = getCsrfToken()

    try {

        const response = await fetch(url, {
            method: 'POST', // HTTP method
            headers: {
                'Content-Type': 'application/json', // Data ka type
                'X-CSRFToken': csrftoken // CSRF token
            },
            body: JSON.stringify(data) // Data ko JSON format mein convert karna
        });

        // Response ko check karna
        if (!response.ok) {
            throw new Error(`Sever Error: Unable to Delete the task.. `);
        }

        // res : Response
        const res = await response.json(); // Response ko JSON format mein convert karna
        console.log('Success:', res); // Success message

        // if we have result and its data then process the add_task
        resFunc(res);


    } catch (error) {
        console.error('Error:', error); // Error handling
    }
}

