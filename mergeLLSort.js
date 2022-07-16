const linkedList = require("./linkedList");

const mergeSort = (list, rev = false) => {
	if (list.sizeOf() <= 1) {
		return list;
	} else if (list.head === undefined) {
		return list;
	}

	let { leftHalf, rightHalf } = divide(list);
	let left = mergeSort(leftHalf, rev);
	let right = mergeSort(rightHalf, rev);

	return sort(left, right, rev);
};

const divide = (list) => {
	const mid = Math.floor(list.sizeOf() / 2);
	const leftHalf = list.slice(0, mid);
	const rightHalf = list.slice(mid);

	return { leftHalf, rightHalf };
};

const sort = (arg1, arg2, rev) => {
	let newList = new linkedList();
	left = arg1.head;
	right = arg2.head;

	if (rev) {
		while (left && right) {
			if (left.data > right.data) {
				newList.append(left.data);
				left = left.nextNode;
			} else {
				newList.append(right.data);
				right = right.nextNode;
			}
		}
		while (left) {
			newList.append(left.data);
			left = left.nextNode;
		}
		while (right) {
			newList.append(right.data);
			right = right.nextNode;
		}

		return newList;
	} else {
		while (left && right) {
			if (left.data < right.data) {
				newList.append(left.data);
				left = left.nextNode;
			} else {
				newList.append(right.data);
				right = right.nextNode;
			}
		}
		while (left) {
			newList.append(left.data);
			left = left.nextNode;
		}
		while (right) {
			newList.append(right.data);
			right = right.nextNode;
		}

		return newList;
	}
};

module.exports = mergeSort;
