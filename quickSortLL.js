const linkedList = require("./linkedList");

const quickSort = (list, rev = false) => {
	if (list.sizeOf() <= 1) {
		return list;
	} else if (list.head === undefined) {
		return list;
	}

	let current = list.head.nextNode;
	const PIVOT = list.head;
	let lessThan = new linkedList();
	let greaterThan = new linkedList();

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
		return (
			quickSort(lessThan, rev) + " " + PIVOT + " " + quickSort(greaterThan, rev)
		);
	} else {
		return (
			quickSort(greaterThan, rev) + " " + PIVOT + " " + quickSort(lessThan, rev)
		);
	}
};
