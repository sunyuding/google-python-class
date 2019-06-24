def main():
  # a = [5, 1, 4, 3]
  # print sorted(a)  ## [1, 3, 4, 5]
  # print a  ## [5, 1, 4, 3]

  # strs = ['aa', 'BB', 'zz', 'CC']
  # print sorted(strs)  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
  # print sorted(strs, reverse=True)  ## ['zz', 'aa', 'CC', 'BB']

  # strs = ['ccc', 'aaaa', 'd', 'bb']
  # print sorted(strs, key=len)

  # print sorted(strs, key=str.lower)

  # strs = ['xc', 'zb', 'yd', 'wa']
  #
  # def MyFn(s):
  #   return s[-1]
  #
  # print sorted(strs, key=MyFn)

  # (x, y, z) = (42, 13, "hike")
  # print z
  # (err_string, err_code) = Foo()

  # nums = [1, 2, 3, 4]
  # squares = [ n * n for n in nums]

  strs = ['hello', 'and', 'goodbye']
  shouting = [s.upper() + '!!!' for s in strs]
  print shouting

if __name__ == '__main__':
  main()
