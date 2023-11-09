from .basket import Basket



# почему-то только в корзине высвечивается ее содержимое, на других странцах такого нет 
def basket(request):
    return {'basket': Basket(request)}