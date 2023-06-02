while True:
  want = input("What do you want for Xmas: (small letters): ")

  if want in ('book', 'phone', 'notebook', 'chocolate'):
      print ("The ", want, " is yours")
      choice = input("do you want something else: 'Y' or 'N':")
      if choice == 'N':
        break
  else:
      print ("I don't have ", want)
