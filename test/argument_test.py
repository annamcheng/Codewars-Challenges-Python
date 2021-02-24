def test_arg(*args):
    return args

a = "hello"
b = [1,2,3]

print(test_arg(a))
print(test_arg(b))
print(test_arg(3,5,7,9))

meerkat = ['head', 'body', 'tail']
myorder = [0,1,2]
mylist = [meerkat[i] for i in myorder]
print(mylist)
# scrambled_meerkat = [body, tail, head]

# def fix_the_meerkat(arr):
#     #your code here
#