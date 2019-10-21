
use std::io;
/* 
   We need to bring the io (input/ output) library into scope. The io
   library comes with a number of useful features, including the ability
   to accept user input. The io library comes from the standard library
   wich is known as std.
*/

use std::cmp::Ordering;
/*
Like Result, Ordering is another enum, but the variants for Ordering are
Less, Great and Equal. These are the three outcomes that are possible 
when you compare two values.
*/

use rand::Rng;


fn main() {
    println!("Guess the number!");
	
	let secret_number = rand::thread_rng().gen_range(1, 101);
	/*rand::thread_rng function will give use the particular random number generator
	  that we're going to use: one that is local to the current thread of execution and
	  seeded by the operating system. Then we call gen_range method on the random number
	  generator , that generates a random number between 1 and 100
	  */
	
	
	loop
	{
	    println!("Please input your guess.");

	    let mut guess = String::new();
	    /* let is used to create a variable, they are immutable by default.
	     Use mut before the variable name to make a variable mutable.
	     String::new is a function that returns a new instance of a String.
	     String is a string type provided by the standard library. 
	     The ::syntax in the ::new line indicates that new is an associated function of
	     the String type. An associated function is implemented on a type, in the case String,
	     rather than on a particular instance of a String. Some language call this a static
	     method. This new function creates a new, empty String. */
	   
	   
	    io::stdin().read_line(&mut guess)
		    .expect("Failed to read line");
			
	    /* Now we'll call the stdin function from the io module, if we hadn't listed the use std::io
	       at the beginning of the program, we could have written this function call as std::io::Stdin,
    	   which is a type that represents a handle to the standard input for your terminal.
    	   The next part of the code, .read_line(&mut guess), calls the read_line method on the standard
	       input handle for get input from the user. We are also passing one argument &mut guess. The
	       job of read_line is to take whatever the user types into standard input and place that into 
	       string, so it takes that string as an argument. The string argument needs to be mutable so
	       the method can change the string's content by adding the user input. The & indicates that
	       this argument is a reference, which gives you a way to let multiple parts of your code access
	       one piece of data without needing to copy that data into memory multiple times. Reference are 
	       immutable by default, so you need to write &mut guess rather than &guess to make it mutable.when you call this method, you
	       can obtain two result of type io::Result, ok or Err.
	       The second part is the method:.expect("Failed to read line"); if readline get an Err that means the operation failed, 
	       its contains information about how or why the operation failed. If this instance of io::Result is an Err value, expect will cause the 
	       program to crash and display the message that you passed as an argument to expect. When you compile you will
	       get a warning, because you haven't used the result value returned from read_line indicating that the program
	       hasn't handled a possible error.
	       */
	
	    let guess: u32 = match guess.trim().parse() {
		    Ok(num) => num,
			Err(_) => continue,
		};
	    /*
	    We cannot compare a String and a number, so we need a conversion of the String input in number. 
	    We have a variable called guess, but Rust allows us to shadow the previous value of guess with 
	    a new one. This feature is often used in situation in which you want to convert a value from
	    one type to another type. Shadowing lets us reuse the guess variable name rather than forcing
	    us to create two unique variables. Trim eliminates the whitespaces. The parse convert the string
	    in the format u32, because let guess: u32, the colon (:) after guess tells Rust we'll annotate the variable's type.
		We're using a match expression, if it returns a Ok value, it just return the number, that number will return in the
		new guess variable. If Err(_), the underscore is a catchall value; in this example we are saying we want ti match
		all Err values, no matter what information they have inside them. So the program continue, which tells to go to the next
		iteration of the loop and ask for another guess.
	    */
	
	    println!("You guessed: {}", guess);
	    	/* This line prints the string we saved the user's input in.
	       	   The set of curly bracket, {}, is a placeholder.
		    */
		
	    match guess.cmp(&secret_number) {
	    	Ordering::Less => println!("Too small!"),
	    	Ordering::Greater => println!("Too big!"),
	    	Ordering::Equal => {
			    println!("You win!");
				break;
			},
	    }
	    /* The cmp methods compare two values and can be called on anything that can be compared. It takes a reference to whatever you want to
           compare with: here it's comparing the guess to secret_number. Then it returns a variant of the Ordering enum we brought into scope with
	       the use statement. We use a match expression to decide what to do next based on which variant of Ordering was returned from the call
	       to cmp with the values in guess and secret_number. A match expression is made up of arms. An arm consiste of a pattern and the code 
	       that should be run if the value given to the beginning of the match expression fits that arm's pattern. Rust takes the value given
	       to match and looks through each arm's pattern in turn.*/
	}
}
