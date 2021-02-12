#include <stdbool.h>
#include <stddef.h>

bool is_c()
{
  size_t value = sizeof 'a';
  if (value == 4) return true;
  return false;
}
