jsx
const handleSubmit = async (recipe) => {
  await fetch('/api/recipes/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(recipe)
  })
}
