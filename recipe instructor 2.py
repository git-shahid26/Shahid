class RecipeInstructor:
    def __init__(self):
        # Dictionary to store recipe data, including ingredients and steps
        self.recipes = {
            'idli': {
                'ingredients': {
                    'Basmati rice': '1/2 cup',
                    'Urad dal': '1/2 cup ',
                    'Fenugreek seeds': '1/2 tablespoon',
                    'sesame oil':'5 tablespoon oil',
                    'salt as required': '1 tsp',
                    'water':'1 cup'
                },
                'steps': [
                    'Wash the idli rice thoroughly and soak it in water for about 4-6 hours',
                    'In a separate bowl, wash the urad dal and fenugreek seeds together and soak them in water for the same duration.',
                    'After soaking, drain the water from both the rice and urad dal.',
                    'Grind the urad dal and fenugreek seeds together in a wet grinder or a high-powered blender. Add water gradually to make a smooth and fluffy batter. The consistency should be similar to that of pancake batter.',
                    'Transfer the urad dal batter to a large bowl.',
                    'Next, grind the soaked rice to a slightly coarse texture. Add water as needed',
                    'Mix the rice batter with the urad dal batter. Add salt to taste and mix well. The consistency should be like a thick pancake batter',
                    'Cover the bowl and let the batter ferment for about 8-12 hours or overnight. Place it in a warm place to aid fermentation. The batter should double in volume.',
                    'Use a butter knife to remove the idlis',
                    'Serve them with Sambhar or chutney',
                    'Grease the idli molds with a little oil or ghee',
                    'Boil water in the idli steamer',
                    'Just before steaming, mix the batter gently. If the batter is too thick, add a little water to achieve the desired consistency.',
                    'Pour the batter into the idli molds, filling them about 3/4 full',
                    'Place the idli molds in the steamer and steam for about 10-15 minutes, or until a toothpick inserted into the center comes out clean',
                    'Allow the idlis to cool for a couple of minutes before removing them from the molds. Use a wet spoon or butter knife to scoop them out',
                    'Serve the idlis hot with coconut chutney and sambar',
                    'Enjoy your homemade idlis'
                ]
            },
            'masala_dosa': {
                'ingredients': {
                    'urad dal (black gram)': '1 cup',
                    'idli rice': '2 cup',
                    'cup poha (flattened rice)': '1/2 cup',
                    'salt': '1 tsp',
                    'water for grinding': '1 cup',
                    'potatoes': '4-5 medium-sized,boiled and mashed',
                    'green chilies': '2-3 finely chopped ',
                    'mustard seeds': '1/2 tsp',
                    'cumin seeds':'1/2 tsp',
                    'asafoetida ':'A pinch',
                    'turmeric powder':'1/2 tsp',
                    'curry leaves':' a Few leaves',
                    'salt':'1 tsp',
                    'oil':'2 tbsp'
                    
                    
                },
                'steps': [
                    'Wash urad dal and idli rice separately. Soak them along with poha in water for about 4-6 hours.',
                    'Grind urad dal, idli rice, and poha together to make a smooth batter. Add water as needed to achieve a pancake batter-like consistency..',
                    'Add salt to the batter, mix well, and let it ferment overnight or for at least 8 hours.',
                    'Heat oil in a pan. Add mustard seeds and cumin seeds. Allow them to splutter',
                    'Add asafoetida, chopped onions, green chilies, and curry leaves. Sauté until the onions turn golden brown.',
                    'Add turmeric powder and mashed potatoes. Mix well',
                    'Cook for a few minutes, stirring occasionally. Add salt to taste. The masala filling is ready. Set it aside',
                    'Heat a non-stick or cast-iron dosa griddle on medium heat',
                    'Once the griddle is hot, pour a ladleful of dosa batter onto the center',
                    'Using the back of the ladle, spread the batter in a circular motion to form a thin, even layer',
                    'Drizzle a little oil around the edges of the dosa. Cook until the bottom turns golden brown and crispy',
                    'Place a portion of the prepared masala filling in the center of the dosa',
                    'Fold the dosa over the filling, creating a semi-circle or roll it into a cylindrical shape',
                    'Repeat the process for the remaining batter and filling.',
                    'Serve hot Masala Dosa with coconut chutney and sambar.',
                    'Enjoy your delicious homemade Masala Dosa!'
                ]
            },
            'chicken_biryani': {
                'ingredients': {
                    'chicken': '500g',
                    'yogurt': '1 cup',
                    'ginger-garlic paste': '1 tablespoon',
                    'red chili powder': '1 tsp',
                    'turmeric powder': ' 1 tsp',
                    'garam masala': '1 tsp',
                    'salt': '2 tsp',
                    'coriander and mint leaves': ' a few bunch of leaves',
                    'basmati rice':'2 cup',
                    'water':'2 litres',
                    'bay leaves':'1-2 leaves',
                    'cloves':'4-5 pieces',
                    'green cardamom':'1-2 pieces',
                    'cinnamon sticks':'1-2 pieces',
                    'thinly sliced onions':'2 large pieces',
                    'Chooped tomatoes':'2 pieces',
                    'cooking oil or ghee':'1/2 cup',
                    'cumin seeds':'1 tsp',
                    'green chilies':'4-5 pieces',
                    'ginger-garlic paste':'1 tbsp',
                    'red chili powder':'1/2 teaspoon',
                    'turmeric powder':'1/2 tsp',
                    'biryani masala (optional)':'1 tsp',
                    'Fresh coriander and mint leaves':'A Few leaves'
                    
                    
                },
                'steps': [
                    'In a bowl, mix together yogurt, ginger-garlic paste, red chili powder, turmeric powder, garam masala, salt, and chopped coriander-mint leaves.',
                    'Add chicken pieces to the marinade, ensuring they are well coated. Cover and let it marinate for at least 1-2 hours, preferably longer in the refrigerator',
                    'Boil water in a large pot. Add soaked and drained basmati rice, bay leaves, whole cloves, whole green cardamom, cinnamon sticks, and salt',
                    'Cook the rice until its 70-80% cooked. It should still have a slight bite to it. Drain the water.',
                    'In a large heavy-bottomed pan, heat oil or ghee. Add cumin seeds and let them splutte',
                    'Cook for a few minutes, stirring occasionally. Add salt to taste. The masala filling is ready. Set it aside',
                    'Add sliced onions and cook until they turn golden brown',
                    'Add ginger-garlic paste and green chilies. Sauté for a minute until the raw smell disappears',
                    'Add chopped tomatoes and cook until they are soft and oil starts separating',
                    'Add red chili powder, turmeric powder, and biryani masala (if using). Mix well',
                    'Add marinated chicken and cook until its partially cooked and the masala coats the chicken well',
                    'Layer the partially cooked rice over the chicken masala. Sprinkle chopped coriander-mint leaves on top',
                    'Seal the pan with aluminum foil or a tight-fitting lid. This is to ensure that the steam doesnt escape',
                    'Cook on low heat (dum) for 20-25 minutes until the chicken is cooked through and the rice is fully cooked',
                    'Alternatively, you can transfer the pot to a preheated oven at 350°F (180°C) for about 25-30 minutes',
                    'Gently fluff the rice with a fork. Serve hot Chicken Biryani with raita or a side salad.',
                    'Enjoy your delicious homemade Chicken Biryani!',

                ]
            },
            'schezwan_noodles': {
                'ingredients': {
                    'noodles (egg noodles or any noodles of your choice)': '200g',
                    'vegetables (carrots, bell peppers, cabbage, and beans), julienned': '1 cup assorted',
                    'Schezwan sauce': '3 tbsp',
                    'soy sauce': '2 tbsp',
                    'ginger-garlic paste': '1 tbsp',
                    'vegetable oil': '1 tbsp',
                    'red chili flakes (adjust to taste)': '1 tsp',
                    'coriander and mint leaves': ' a few bunch of leaves',
                    'vinegar':'1 tsp',
                    'salt':'1 tsp',
                    'coriander leaves for garnish (optional)':'A Few leaves'
                    
                    
                    
                },
                'steps': [
                    'Boil the noodles according to the package instructions until they are al dente. Drain and set aside. You can toss them with a little oil to prevent sticking.',
                    'Heat oil in a wok or a large pan. Add ginger-garlic paste and sauté for a minute.',
                    'Add the julienned vegetables and stir-fry over high heat until they are cooked but still retain their crunch. This usually takes 3-5 minutes.',
                    'Push the vegetables to the side of the wok, creating a well in the center',
                    'Add Schezwan sauce, soy sauce, red chili flakes, vinegar, and salt to the well. Mix the sauces together in the well.',
                    'Combine the sauces with the vegetables. Toss the cooked noodles into the sauce-vegetable mixture.',
                    'Stir-fry the noodles and vegetables together, ensuring the noodles are well coated with the Schezwan sauce. Use chopsticks or tongs for better mixing.',
                    'Once the noodles are heated through and evenly coated with the sauce, remove from heat',
                    'Garnish with fresh coriander leaves if desired.',
                    'Serve Schezwan Noodles hot, either on their own or with a side of vegetable Manchurian or a cooling cucumber salad.',
                    'Enjoy your homemade Schezwan Noodles!',

                ]
            },
            'bhel_puri': {
                'ingredients': {
                    'puffed rice(murmura)': '4 cups',
                    'sev (thin chickpea flour noodles)': '1 cup',
                    'boiled and chopped potatoes': '1 cup',
                    'chopped tomatoes': '1 cup',
                    'chopped onions': '1/2 cup',
                    'chopped cucumber': '1 tbsp',
                    'chopped raw mango (optional, for a tangy flavor)': '1/2 cup',
                    'coriander and mint leaves': ' a few bunch of leaves',
                    'chopped coriander leaves':'1/4 cup',
                    'chopped mint leaves':'1/4',
                    'tamarind chutney':'1/2 cup',
                    'green chutney':'2 tbsp ',
                    'chaat masala':'1 tsp',
                    'roasted cumin powder':'1/2 tsp',
                    'salt':'1 tsp',
                    'Pomegranate seeds for garnish (optional)':'1/2 cup',
                    'Lemon wedges':'1 slice'
                    
                    
                },
                'steps': [
                    'Boil and chop the potatoes.',
                    'Chop tomatoes, onions, cucumber, raw mango (if using), coriander leaves, and mint leaves.',
                    'In a large mixing bowl, combine puffed rice, sev, boiled potatoes, tomatoes, onions, cucumber, raw mango, coriander leaves, and mint leaves.',
                    'Add tamarind chutney and green chutney to the mixture. Adjust the quantity according to your taste preference.',
                    'Sprinkle chaat masala, roasted cumin powder, and salt over the mixture.',
                    'Gently toss all the ingredients together, making sure that the chutneys and spices are evenly distributed.',
                    'Garnish the Bhel Puri with pomegranate seeds (if using). This adds a burst of sweetness and freshness.',
                    'Serve Bhel Puri immediately in individual bowls or plates.',
                    'Squeeze some fresh lemon juice over the Bhel Puri just before eating to enhance the flavors',
                    'Mix the Bhel Puri well before eating to ensure that all the flavors are combined. Its meant to be eaten immediately to retain its crispiness.',
                    'Enjoy your homemade Bhel puri',

                ]
            },
        }

    def get_recipe(self, dish):
        
        """Display the ingredients, amounts, and steps needed for a given dish."""
        
        dish = dish.lower().replace(' ', '_') # Convert input to lowercase and replace spaces with underscores
        
        if dish in self.recipes:
            print(f"Recipe for {dish.replace('_', ' ')}:")
            print("\nIngredients:")
            for ingredient, amount in self.recipes[dish]['ingredients'].items():
                print(f"{ingredient}: {amount}")

            print("\nSteps:")
            for i, step in enumerate(self.recipes[dish]['steps'], 1):
                print(f"{i}. {step}")
        else:
            print(f"Sorry, the recipe for {dish.replace('_', ' ')} is not available.")

def main():
    instructor = RecipeInstructor()

    while True:
        user_input = input("Enter the dish you want to make (or 'exit' to quit): ").lower()

        if user_input == 'exit':
            break

        instructor.get_recipe(user_input)

if __name__ == "__main__":
    main()
