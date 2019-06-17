def main():
  # a = [5, 1, 4, 3]
  # print sorted(a)  ## [1, 3, 4, 5]
  # print a  ## [5, 1, 4, 3]

  strs = ['aa', 'BB', 'zz', 'CC']
  print sorted(strs)  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
  print sorted(strs, reverse=True)  ## ['zz', 'aa', 'CC', 'BB']

if __name__ == '__main__':
  main()
