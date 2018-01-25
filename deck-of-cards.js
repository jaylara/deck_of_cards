var prompt = require('./js-tools/prompt-sync')();
var yn = require('./js-tools/yn');

// 1. Create an array of cards using suits and values.
// Each card in the deck should be an object formatted as: {suit}{value}
function deck_o_cards() {
  var values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'];
  var suits = ['♥', '♦', '♣', '♠'];
  var cards = []; // deck
  var shuffledCards = []; // deck shuffled

  // Make 52 card objects and store them in the "cards" array
  for (var s = 0; s < suits.length; s++) {
    for(var v = 0; v < values.length; v++) {
      cards.push({suit: suits[s], value: values[v]});
    }
  }

  // 2. Shuffle the cards
  shuffledCards = shuffle(cards);

  // 3. Print the results:
  console.log(`The Original Deck has ${cards.length} cards.`);
  console.log(`The top card is ${cardToString(cards[0])}`);
  printFullDeck(cards);
  console.log("----");
  console.log(`The Shuffled Deck has ${shuffledCards.length} cards.`);
  console.log(`The top card is ${cardToString(shuffledCards[0])}`);
  printFullDeck(shuffledCards);

  // Pull the top 5 cards and display
  console.log("----");
  var draw = prompt("How many cards would you like to draw? ");
  for (var i = 0; i < draw; i++)
    console.log(`Draw ${i+1}:\t${cardToString(shuffledCards.shift())}`);
}

var printFullDeck = function(cards) {
  for(var v = 0; v <13; v++) {
    var str = "";
    for(var c = 0; c<52; c+=13)
      str += `${cardToString(cards[v+c])}\t`;
    console.log(str);
  }//end of for
}

var cardToString = function(card) {
  return `${card.suit}${card.value}`;
}

deck_o_cards();

// Fisher-Yates Shuffle: http://stackoverflow.com/a/6274398
function shuffle(originalArray) {
    var array = JSON.parse(JSON.stringify(originalArray));
    var counter = array.length, temp, index;

    // While there are elements in the array
    while (counter > 0) {
        index = Math.floor(Math.random() * counter); // Pick a random index
        counter--; // Decrease counter by 1

        // And swap the last element with it
        temp = array[counter];
        array[counter] = array[index];
        array[index] = temp;
    }

    return array;
}
