from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeCategoryView(RecipeTestBase):
    def test_function_category_view_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_status_code_is_200_OK(self):
        self.make_recipe()
        response = self.client.get(reverse(
            'recipes:category', kwargs={'category_id': 1})
            )
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_view_returns_404_if_no_recipe_found(self):
        response = self.client.get(reverse(
            'recipes:category', kwargs={'category_id': 1000})
            )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category page test'
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn('This is a category page test', content)

    def test_recipe_category_dont_show_recipes_if_is_published_false(self): # noqa E501
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse(
            'recipes:category', kwargs={'category_id': recipe.category.id})
            )
        self.assertEqual(response.status_code, 404)