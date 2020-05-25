// a new way of declaring function
const game = ()=> {
    // intial score
    let pScore = 0;
    let cScore=0;

    // starting the game
    const startGame = () => {
        const playBtn = document.querySelector('.intro button');
        const introScreen = document.querySelector('.intro');
        const match = document.querySelector('.match');

        // fade out + fadeIn of the initial Screen
        playBtn.addEventListener("click", () => {
            introScreen.classList.add("fadeOut");
            match.classList.add("fadeIn");
        });
    };

    // play match
    const playMatch = () => {
        const options = document.querySelectorAll(".options button");
        const playerHand = document.querySelector(".player-hand");
        const computerHand = document.querySelector(".computer-hand");

        const hands = document.querySelectorAll(".hands img");

        hands.forEach(hand => {
            hand.addEventListener("animationend", function(){
                this.style.animation = "";
            });
        });
        // generating computer options
        const computerOptions = ['rock', 'paper', 'scissors'];
        
        options.forEach(option => {
            option.addEventListener("click", function() {
            //Computer Choice
            const computerNumber = Math.floor(Math.random() * 3);
            const computerChoice = computerOptions[computerNumber];
  
            setTimeout(() => {
                //Here is where we call compare hands
                compareHands(this.textContent, computerChoice);
                //Update Images
                playerHand.src = `design/${this.textContent}.png`;
                computerHand.src = `design/${computerChoice}.png`;
                // added 2000 ms delay
            }, 2000);
            //Animation
            playerHand.style.animation = "shakePlayer 2s ease";
            computerHand.style.animation = "shakeComputer 2s ease";
            });
        });
        };

    // updating score
    const updateScore = () =>{
        const playerScore = document.querySelector(".player-score p");
        const computerScore = document.querySelector(".computer-score p");
        playerScore.textContent = pScore;
        computerScore.textContent = cScore;
    }

    const compareHands = (playerChoice, computerChoice) =>{
        
        const winner = document.querySelector('.winner');
        // check for a tie
        if (playerChoice===computerChoice){
            winner.textContent = "It is a TIE!!";
        }
        // checking for rock
        if (playerChoice==='rock'){
            if(computerChoice==='paper'){
                // Updating text
                winner.textContent = "Computer Wins";
                // Incrementing Score
                cScore++;
                // Updating Score
                updateScore();
                return;
            }
            if(computerChoice==='scissors'){
                winner.textContent = "Player Wins";
                pScore++;
                updateScore();
                return;
            }
        }
        // checking for paper
        if (playerChoice==='paper'){
            if(computerChoice==='scissors'){
                winner.textContent = "Computer Wins";
                cScore++;
                updateScore();
                return;
            }
            if(computerChoice==='rock'){
                winner.textContent = "Player Wins";
                pScore++;
                updateScore();
                return;
            }
        }
        // checking for scissors
        if (playerChoice==='scissors'){
            if(computerChoice==='rock'){
                winner.textContent = "Computer Wins";
                cScore++;
                updateScore();
                return;
            }
            if(computerChoice==='paper'){
                winner.textContent = "Player Wins";
                pScore++;
                updateScore();
                return;
            }
        }
    }


    // calling inner function
    startGame();
    playMatch();
}

// calling main function
game();