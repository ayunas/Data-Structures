// # Print out all of the numbers in the following array that are divisible by 3:
// # [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
// # You may use whatever programming language you wish.




const arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

divthrees = arr.filter(num => num % 3 === 0)

console.log(divthrees)

