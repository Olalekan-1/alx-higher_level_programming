#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - To print the info of a list
 * @p: pointer to the list object
 * Return: void, but print the info
 */


void print_python_list_info(PyObject *p)
{
	PyListObject *List = (PyListObject *)p;
	int i;
	long int size = PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", List->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(List->ob_item[i])->tp_name);
	}
}
