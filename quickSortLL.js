// FIXME - fix quicksort function to return a linked list

// const linkedList = require("./linkedList");

// const quickSort = (list, rev = false) => {
// 	if (list.sizeOf() <= 1) {
// 		return list;
// 	} else if (list.head === undefined) {
// 		return list;
// 	}

// 	let current = list.head.nextNode;
// 	const PIVOT = list.head;
// 	const lessThan = new linkedList();
// 	const greaterThan = new linkedList();

// 	while (current) {
// 		if (current.data <= PIVOT.data) {
// 			lessThan.append(current.data);
// 			current = current.nextNode;
// 		} else {
// 			greaterThan.append(current.data);
// 			current = current.nextNode;
// 		}
// 	}

// 	if (rev) {
// 		return (
// 			quickSort(lessThan, rev) + " " + PIVOT + " " + quickSort(greaterThan, rev)
// 		);
// 	} else {
// 		return (
// 			quickSort(greaterThan, rev) + " " + PIVOT + " " + quickSort(lessThan, rev)
// 		);
// 	}
// };

// module.exports = quickSort;

// let a = new linkedList();
// a.append(327);
// a.append(332);
// a.append(132);
// a.append(2);
// a.append(3);

// let l = quickSort(a);
// console.log(l);

// quickSort(a);

const linkedList = require("./linkedList");

const quickSort = (list, rev = false) => {
	if (list.sizeOf() <= 1) {
		return list;
	} else if (list.head === undefined) {
		return list;
	}

	// compare(list, rev);

	let current = list.head.nextNode;
	const PIVOT = list.head;
	const lessThan = new linkedList();
	const greaterThan = new linkedList();
	let newList;

	while (current) {
		if (current.data <= PIVOT.data) {
			lessThan.append(current.data);
			current = current.nextNode;
		} else {
			greaterThan.append(current.data);
			current = current.nextNode;
		}
	}
	if (rev) {
		newList = lessThan.slice();
		newList.prepend(PIVOT.data);
		// newList.prepend(greaterThan.slice());
	} else {
		newList = lessThan.slice();
		newList.append(PIVOT.data);
		// newList.append(greaterThan.slice());
	}

	return newList;

	// return quickSort(list, rev);
};

const compare = (list, rev) => {};

module.exports = quickSort;

let a = new linkedList();
a.append(327);
a.append(332);
a.append(132);
a.append(2);
a.append(3);

let l = quickSort(a);
// console.log(l);
l.showAllNodes();
