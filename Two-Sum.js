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
