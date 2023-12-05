#include <python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)P;

	printf("[*] size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %: %s\n", i, Py-TYPE(obj->ob_item[i])->tp_name);
}
