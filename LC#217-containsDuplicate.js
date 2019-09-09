var containsDuplicate = function(nums) {
  var obj = {};
	for(let i = 0; i < nums.length; i++){
		if(!obj[nums[i]]){
			obj[nums[i]] = true;
		}
		else{
			return true;
		}
	}
	return false;
};

//O(n) - Time Complexity
//O(n) - Space Complexity
