# что такое глубокая копия ( deep copy ) в отличии от обычной которая .pop )
import copy
original_list = [1, 2, 3, ["a", "b", "c"]]
copy_of_original_list = copy.deepcopy(original_list) # Создает полную копию оригинального списка со всеми элементами ( в этом и разница с обычной копией)
original_list[3] = 4                                 # меняем значение но так как мы выполнили дипкопию то у нас теперь и оригинал сохранился и ихменения
print(original_list)
print(copy_of_original_list)