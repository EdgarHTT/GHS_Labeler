export function fetchCompound(compoundName) {
    return fetch('http://localhost:5000/compoundName', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({compoundName})
    })
    .then(data => data.json())
}