//Declare an array named "alphabet" by the type of Character
let alphabet : [Character] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

//Define a variable called secretMessage
var secretMessage = "Hello"

//Be sure that the message is lowercased, because of our alphabet definer for just lowercase letters
secretMessage = secretMessage.lowercased()

//Used Swift array initializer, that spells the characters of the string
//output: ["h","e","l","l","o"]
var message = Array(secretMessage)

//the loop continues if iterated less than the count of message
for i in 0 ..< message.count {
  //the inner loop continues if iterated less than the count of alphabet
  for j in 0 ..< alphabet.count {
    //if character matches, make it the 3rd next character for the Caesar Cipher encryption.
    if message[i] == alphabet[j] {
      message[i] = alphabet[(j+3) % 26]
      break
    }
  }
}
//Convert the final result of Array to the String, and print it
let finalRes = message.map{String($0)}.joined(separator: "")
print(finalRes)
