#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_list - To print the info of a list
 * @p: pointer to the list object
 * Return: void, but print the info
 */



void print_python_list(PyObject *p)
{
	PyListObject *List = (PyListObject *)p;
	int i = 0;
	long int size = ((PyVarObject *)(p))->ob_size;
	PyObject *lists;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", List->allocated);
	for (i = 0; i < size; i++)
	{
		lists = ((PyListObject *)p)->ob_item[i];
		printf("Element %i: %s\n", i, ((lists)->ob_type)->tp_name);
		if (PyBytes_Check(lists))
			print_python_bytes(lists);
	}
}


/**
 * print_python_bytes - print the byte strings of an object
 * @p: pointer to the object
 * Return: void ...
 */

void print_python_bytes(PyObject *p)
{
	char *bytes_string = ((PyBytesObject *)p)->ob_sval;
	long int size = ((PyVarObject *)(p))->ob_size, i, lim;

	printf("[.] bytes object info\n");
	/* check if it is PybytesObject */
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", bytes_string);
	if (size >= 10)
	{
		lim = 10;
	}
	else
		lim = size + 1; /* plus the null character */
	printf("  first %li bytes:", lim);
	for (i = 0; i < lim; i++)
	{
		if (bytes_string[i] >= 0)
			printf(" %02x", bytes_string[i]); /* print in hex */
		else
			printf(" %02x", 256 + bytes_string[i]); /* add null char */
	}
	putchar(10);
}

