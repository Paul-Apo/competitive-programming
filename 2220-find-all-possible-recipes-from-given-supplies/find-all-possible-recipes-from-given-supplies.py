class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Convert supplies to a set for O(1) lookup
        available = set(supplies)
        # Result list to store producible recipes
        result = []
        
        # Build the graph: recipe -> ingredients needed
        graph = defaultdict(list)
        # Track in-degree (number of ingredients needed for each recipe)
        in_degree = defaultdict(int)
        
        # Construct the graph and in-degree counts
        for recipe, ingredient_list in zip(recipes, ingredients):
            for ingredient in ingredient_list:
                # If ingredient is not in supplies, it must be a recipe we need to make
                if ingredient not in available:
                    graph[ingredient].append(recipe)
                    in_degree[recipe] += 1
            # If recipe has no missing ingredients, it can potentially be made
            if recipe not in in_degree:
                in_degree[recipe] = 0
        
        # Initialize queue with recipes that have all ingredients available
        queue = deque([recipe for recipe in recipes if in_degree[recipe] == 0])
        
        # Process recipes using topological sort
        while queue:
            curr_recipe = queue.popleft()
            result.append(curr_recipe)
            # Treat the recipe as available now (like a new supply)
            available.add(curr_recipe)
            
            # Process all recipes that depend on curr_recipe
            for next_recipe in graph[curr_recipe]:
                in_degree[next_recipe] -= 1
                # If all ingredients for next_recipe are available, add it to queue
                if in_degree[next_recipe] == 0:
                    queue.append(next_recipe)
        
        return result
            