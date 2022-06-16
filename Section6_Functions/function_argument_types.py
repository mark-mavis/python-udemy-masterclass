def func(position1, position2, *args, keyword, **kwargs):
  print("positional-or-keyword:...{}, {}".format(p1, p2))
  print("var-positional (*args):..{}".format(args))
  print("keywords:................{}".format(k))
  print("var-keyword:.............{}".format(kwargs))
  

func(1, 2, 3, 4, 5, keyword=6, key1=7, key2=8, key3=9, key4=10)