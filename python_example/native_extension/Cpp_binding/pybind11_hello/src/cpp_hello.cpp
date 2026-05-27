#include <pybind11/pybind11.h>
#include <string>

namespace py = pybind11;

class Hello {
public:
    explicit Hello(std::string name) : name_(std::move(name)){}

    std::string greet() const {
        return "hello, " + name_ + " from C++!";
    }

private:
    std::string name_;
};

int add(int left, int right){
    return left + right;
}

PYBIND11_MODULE(cpp_hello, module){
    module.doc() = "Small pybind11 example module";
    module.def("add", &add, "Add two integers");

    py::class_<Hello>(module, "Hello")
        .def(py::init<std::string>())
        .def("greet", &Hello::greet);
}