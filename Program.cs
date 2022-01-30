// See https://aka.ms/new-console-template for more information

using GuessNumber;

var game = new InitGame();
game.StartGameInstance();

var keepPlaying = true;

while (keepPlaying)
{

    Console.WriteLine("Please make a guess");
    var guess = int.Parse(Console.ReadLine() ?? string.Empty);
    game.MakeGuess(guess);


    Console.WriteLine("Do you want to guess again? Y/N");
    var decision = Console.ReadKey();
    Console.WriteLine(Environment.NewLine);

    if (decision.KeyChar != 'Y' && decision.KeyChar != 'y')
    {
        keepPlaying = false;
    }
}

