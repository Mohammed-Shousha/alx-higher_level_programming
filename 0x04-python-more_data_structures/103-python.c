#include <stdio.h>
#include <Python.h>
#include "/usr/include/python3.4/bytesobject.h"

/**
 * print_python_bytes - print some basic info about Python bytes objects
 * @p: python object
 * Return: void
 **/

void print_python_bytes(PyObject *p)
{
  char *s;
  Py_ssize_t len, i;

  printf("[.] bytes object info\n");
  if (!PyBytes_Check(p))
  {
    printf("  [ERROR] Invalid Bytes Object\n");
    return;
   }

  PyBytes_AsStringAndSize(p, &s, &len);
  printf("  size: %ld\n", len);
  printf("  trying string: %s\n", s);

  len = len > 10 ? 10 : len + 1;

  printf("  first %ld bytes: ", len);

  for (i = 0; i < len - 1; i++)
    printf("%02x ", s[i] & 0xff);

  printf("%02x\n", s[len - 1] & 0xff);
}


/**
 * print_python_list - print some basic info about Python lists
 * @p: python object
 * Return: void
 **/
void print_python_list(PyObject *p)
{
  Py_ssize_t i, size;
  PyObject *in_list;

  if (!PyList_Check(p))
    return;

  size = PyList_Size(p);

  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %lu\n", size);
  printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

  for (i = 0; i < size; i++)
  {
    in_list = PyList_GetItem(p, i);
    printf("Element %lu: %s\n", i, in_list->ob_type->tp_name);

    if (strcmp(in_list->ob_type->tp_name, "bytes") == 0)
      print_python_bytes(in_list);
  }
}
