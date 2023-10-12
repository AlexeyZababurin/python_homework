# Задача 44: В ячейке ниже представлен код генерирующий whoAmIFrame, которая 
# состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?
#
# import random
# import pandas as pd
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# whoAmI = pd.whoAmIFrame({'whoAmI':lst})
# whoAmI.head()


import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
whoAmI = pd.DataFrame({'whoAmI': lst})
print(whoAmI)
print('')

whoAmI['tmp'] = 1
whoAmI.set_index([whoAmI.index, 'whoAmI'], inplace=True)
whoAmI = whoAmI.unstack(level=-1, fill_value = 0).astype(int)
whoAmI.columns = whoAmI.columns.droplevel()
print(whoAmI)
