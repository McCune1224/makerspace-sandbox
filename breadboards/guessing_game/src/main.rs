use std::{cmp::Ordering, io};

use rand::Rng;

fn main() {
    // Prompt user for number
    println!("Welcome to my guessing game!");
    println!("Guess a number between 1 and 3 !");

    //variables to use for guessing game
    let secret_number = rand::thread_rng().gen_range(1..=3);
    let mut guess = String::new();

    // attempt to grab user input
    io::stdin()
        .read_line(&mut guess)
        .expect("Unable to read line");
    // attempt to parse user input from string to
    let guess: u32 = guess.trim().parse().expect("Please type a number!");

    println!("You guessed {guess}");
    match guess.cmp(&secret_number) {
        Ordering::Less => println!("Too Low"),
        Ordering::Equal => println!("Spot on! The secret number was {secret_number}"),
        Ordering::Greater => println!("Too Big"),
    }
}
