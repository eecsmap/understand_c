int main()
{
  // what is returned depends on how compiler understand this expression
  // left associated: (1 ? 2 : 3) ? 4 : 5
  // right associated: 1 ? 2 : (3 ? 4 : 5)
  // understand this can help you write the correct production grammar for conditional expression
  return 1 ? 2 : 3 ? 4 : 5;
}
