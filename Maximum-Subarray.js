//Brute Force Solution//
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

//----------

//Efficient Solution using Kadane's Algorithm//
var maxSubArray = function(nums){

	let globalMaximum = nums[0];
	let currentMaximum = nums[0];

	for(let i=1; i<(nums.length-1); i++){
		currentMaximum = Math.max(nums[i], currentMaximum + nums[i]);
		if(globalMaximum < currentMaximum){
			globalMaximum = currentMaximum;
		}
	}
	return globalMaximum
}

console.log(maxSubArray([8,9,-5,20]));
//O(n) - Time Complexity
//O(1) - Space Complexity
