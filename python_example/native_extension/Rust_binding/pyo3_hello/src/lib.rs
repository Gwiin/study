use pyo3::prelude::*;

#[pyfunction]
fn make_greeting(name: &str) -> String {
    format!("hello, {name} from Rust!")
}

#[pyfunction]
fn add(left: i64, right: i64) -> i64 {
    left + right
}

#[pymodule]
fn rust_hello(module: &Bound<'_, PyModule>) -> PyResult<()> {
    module.add_function(wrap_pyfunction!(make_greeting, module)?)?;
    module.add_function(wrap_pyfunction!(add, module)?)?;
    Ok(())
}