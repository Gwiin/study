#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

static PyObject *make_greeting(PyObject * self, PyObject *args)
{
    const char *name;

    if(!PyArg_ParseTuple(args, "s", &name))
    {
        return NULL;
    }
    return PyUnicode_FromFormat("hello, %s!", name);
}

static PyObject *print_hello(PyObject *self, PyObject *args)
{
    printf("Hello from a small C extension!\n");
    Py_RETURN_NONE;
}

static PyMethodDef HelloCoreMethods[] = {
    {"make_greeting", make_greeting, METH_VARARGS, "Return a greeting message"},
    {"print_hello", print_hello, METH_NOARGS, "Print a hello message."},
    {NULL,NULL,0, NULL}

};

static PyModuleDef hello_core_module = {
    PyModuleDef_HEAD_INIT,
    "_hello_core",
    "Small C functions used by the Python wrapper",
    -1,
    HelloCoreMethods
};

PyMODINIT_FUNC PyInit__hello_core(void)
{
    return PyModule_Create(&hello_core_module);
}
