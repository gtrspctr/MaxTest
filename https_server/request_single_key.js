// POST request handler where a user may request the value for a key
// NOT WORKING
var value = prompt("What key would you like to lookup? ");


fetch('https://alrobison.com/users')
    .then(response => response.json())
    .then(data => console.log(data))
