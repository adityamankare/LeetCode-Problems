// --- Brute Force Solution - O(n^2) 
var twoSum = function (nums, target) {
    var resultArray = [];

    for (var i = 0; i < nums.length; i++) {
        for (var j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                resultArray.push(i);
                resultArray.push(j);
            }
        }
    }
    return resultArray;
}
console.log(twoSum([2, 7, 11, 15], 9));



// --- Efficient Solution which accounts for Time Complexity and Space Complexity = O(n)
var twoSum = function(nums, target){

	var obj = {};
	var resultArray = [];

	for( let i = 0; i < nums.length; i++){
		if(obj.hasOwnProperty(nums[i])){
			resultArray[0] = obj[nums[i]];
			resultArray[1] = i;
			return resultArray;
		}
		else{
			obj[target-nums[i]] = i;
		}
	}
}

//twoSum([2, 7, 11, 15], 26);
