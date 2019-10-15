use std::io::{self, Read};
fn main() -> io::Result<()>{
  let mut a = String::new();
  let fib1 = 0;
  let fib2 = 1;
  while fib2 <= a{
    fib = fib1 + fib2;
    fib1 = fib2;
    fib2 = fib;
  }
  let n = fib1 + fib2;
  writeln!(n);
  }