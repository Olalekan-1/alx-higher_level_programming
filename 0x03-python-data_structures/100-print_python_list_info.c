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
	size_t itemAllocated;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid list object\n");
		return;
	}
	size = PyList_Size(p);

	if (size < 0)
	{
		fprintf(stderr, "Failed to get list size\n");
		return;
	}
	printf("[*] Size of the Python List = %zd\n", size);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		itemstr =  PyObject_Str(item);
		itemCstr = PyUnicode_AsUTF8(itemstr);

		if (itemstr == NULL || itemCstr == NULL)
		{
			Py_DECREF(itemstr);
			Py_DECREF(item);
			fprintf(stderr, "Failed to convert item to string at index %zd\n", i);
			return;
		}
		itemAllocated = (item->ob_type->tp_basicsize);
		printf("[*] Allocated = %zd\n", itemAllocated);
		printf("Element %zd: %s\n", i, itemCstr);
		
		Py_DECREF(itemstr);
	/*	Py_DECREF(item);
		PyObject_Free((void *)itemAllocated);*/
	}
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		Py_DECREF(item);
	}
	/*PyObject_Free((void *)itemAllocated);*/

}

