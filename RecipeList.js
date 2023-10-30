const fetchRecipes = async () => {
  const response = await fetch('/api/recipes/')
  const data = await response.json()

  setRecipes(data) 
}