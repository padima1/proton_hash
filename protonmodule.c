#include <Python.h>

#include "proton.h"

static PyObject *proton_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    proton_hash((char *)PyBytes_AsString((PyObject*) input), (int)PyBytes_Size((PyObject*) input), output);
#else
    proton_hash((char *)PyString_AsString((PyObject*) input), (int)PyString_Size((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef ProtonMethods[] = {
    { "getPoWHash", proton_getpowhash, METH_VARARGS, "Returns the proof of work hash using proton hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef ProtonModule = {
    PyModuleDef_HEAD_INIT,
    "proton_hash",
    "...",
    -1,
    ProtonMethods
};

PyMODINIT_FUNC PyInit_proton_hash(void) {
    return PyModule_Create(&ProtonModule);
}

#else

PyMODINIT_FUNC initproton_hash(void) {
    (void) Py_InitModule("proton_hash", ProtonMethods);
}
#endif
