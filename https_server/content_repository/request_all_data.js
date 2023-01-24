// POST request handler where a user may request all
// the current contents of the key-value structure

//fetch('/users') local
fetch('https://alrobison.com/users')
    .then(response => response.json())
    .then(data => console.log(data))
