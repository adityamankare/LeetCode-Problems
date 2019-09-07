//Brute Force Solution
function maximumSubArray(arr){

	let maximumSum = -Infinity;
	let currentSum;

	for(let i = 0; i < arr.length; i++){
		currentSum = 0;
		for(let j = i; j < arr.length; j++){ 
			currentSum += arr[j];
			if(maximumSum < currentSum){
				maximumSum = currentSum;
			}
		}
	}
	return maximumSum;
}

console.log(maximumSubArray([2,5,11,-15]));

//O(n^2) - Time Complexity
//O(1) - Space Complexity
