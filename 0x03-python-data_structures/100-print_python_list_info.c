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
	PyObject *item;
	Py_ssize_t size, i;
	PyObject *itemstr;
	const char *itemCstr;

	size = PyList_Size(p);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		itemstr = PyObject_Str(item);
		itemCstr = PyUnicode_AsUTF8(itemstr);
		printf("%s\n", itemCstr);
		Py_DECREF(itemstr);
	}
}

