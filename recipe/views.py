@api_view(['POST'])
def create_recipe(request):
  data = request.data

  recipe = Recipe.objects.create(
    title=data['title'], 
    ingredients=data['ingredients'],
    instructions=data['instructions'],
    time=data['time']
  )
  
  return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_recipes(request):
  recipes = Recipe.objects.all()
  serializer = RecipeSerializer(recipes, many=True)
  return Response(serializer.data)  