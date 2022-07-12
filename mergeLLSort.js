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
	let current = list.head;
	let leftHalf = new linkedList();
	let rightHalf = new linkedList();
	let size = list.sizeOf();

	for (let i = 0; i < size; i++) {
		if (i < Math.floor(size / 2)) {
			leftHalf.append(current.data);
			current = current.nextNode;
		} else {
			rightHalf.append(current.data);
			current = current.nextNode;
		}
	}

	return { leftHalf, rightHalf };
};

const sort = (arg1, arg2, rev) => {
	let newlinkedList = new linkedList();
	left = arg1.head;
	right = arg2.head;

	if (rev) {
		while (left && right) {
			if (left.data > right.data) {
				newlinkedList.append(left.data);
				left = left.nextNode;
			} else {
				newlinkedList.append(right.data);
				right = right.nextNode;
			}
		}
		while (left) {
			newlinkedList.append(left.data);
			left = left.nextNode;
		}
		while (right) {
			newlinkedList.append(right.data);
			right = right.nextNode;
		}

		return newlinkedList;
	} else {
		while (left && right) {
			if (left.data < right.data) {
				newlinkedList.append(left.data);
				left = left.nextNode;
			} else {
				newlinkedList.append(right.data);
				right = right.nextNode;
			}
		}
		while (left) {
			newlinkedList.append(left.data);
			left = left.nextNode;
		}
		while (right) {
			newlinkedList.append(right.data);
			right = right.nextNode;
		}

		return newlinkedList;
	}
};
