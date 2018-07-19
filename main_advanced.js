var playGame = function() {
   var compPick = function() {
      randomNum = Math.random();
      //Computer decision
      if (randomNum < 0.34) {
         return "rock";
      } else if (randomNum <= 0.67) {
         return "paper";
      } else {
         return "scissors";
      }
   };

   //Players decisions
   var playAgain = false;
   var userChoice = prompt("Do you choose 'rock', 'paper' or 'scissors'?").toLowerCase();
   var computerChoice = compPick();

   //compare each player's choices
   var compare = function(choice1, choice2) {
      if (choice1 === choice2) {
         computerChoice = compPick();
         userChoice = prompt("The result is a tie! Try again. 'Rock', 'paper', or 'scissors'");
         return compare(userChoice, computerChoice);
      } else if (choice1 === "rock") {
         if (choice2 === "scissors") {
            return "You win!";
         } else {
            return "Computer wins..";
         }
      } else if (choice1 === "paper") {
         if (choice2 === "rock") {
            return "You win!";
         } else {
            return "Computer wins..";
         }
      } else if (choice1 === "scissors") {
         if (choice2 === "paper") {
            return "You win!"
         } else {
            return "Computer wins"
         }
      }
      //user wrong choice
      else {
         userChoice = prompt("ERROR: Your input must be 'rock', 'paper', or 'scissors'. Choose one of these options again.");
         computerChoice = compPick();
         return compare(userChoice, computerChoice);
      }
   };

   var winner = compare(userChoice, computerChoice);
   alert("You chose: " + userChoice + "\n" + "Computer chose: " + computerChoice + "\n" + winner);
   var playGameAgain = function() {
      userAnswer = prompt("Play again? Yes or no?").toLowerCase();
      if (userAnswer === "yes") {
         return playGame();
      }
      if (userAnswer === "no") {
         alert("Thanks for playing")
      } else {
         userAnswer = alert("ERROR: Response has to be 'yes' or 'no'. Try again.");
         return playGameAgain();
      }
   };
   while (playGameAgain() === true);
};
playGame();

