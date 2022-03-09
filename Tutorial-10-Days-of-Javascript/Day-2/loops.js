"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", (_) => {
  inputString = inputString
    .trim()
    .split("\n")
    .map((string) => {
      return string.trim();
    });

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
  // Split the string into vowels and consonants
  let vowels = [];
  let consonants = [];
  /*
   * Loop through the string where if its a vowel then push into vowels array
   * Otherwise push to the consonants array
   */
  for (let i = 0; i < s.length; i++) {
    switch (true) {
      case "aiueo".includes(s[i]):
        vowels.push(s[i]);
        break;
      default:
        consonants.push(s[i]);
    }
  }
  // Console log the vowels
  for (let i = 0; i < vowels.length; i++) {
    console.log(vowels[i]);
  }
  // Console log the consonants
  for (let i = 0; i < consonants.length; i++) {
    console.log(consonants[i]);
  }
}
