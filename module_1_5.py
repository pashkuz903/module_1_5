immutable_var = 1, 2.5, 'Hello', True
print(immutable_var)
#immutable_var[0] = 5 (в кортеже нельзя изминить элемент, так как это не изменяемая коллекция. Исключение составляют случаи, когда внутри кортежа находится список!)
mutable_var = [2, 4.5, 'Goodbye', False]
print(mutable_var)
mutable_var[0] = 6
mutable_var[2] = 'Досвидания'
mutable_var[3] = True
print(mutable_var)
