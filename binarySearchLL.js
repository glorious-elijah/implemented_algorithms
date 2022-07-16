const binarySearch = (list, key) => {
	if (list.sizeOf() < 1) {
		return list;
	}
	if (list.head === undefined) {
		return list;
	}

	const midPoint = Math.floor(list.sizeOf() / 2);
	const current = list.atIndex(midPoint);
	let newList;

	if (key === current.data) {
		return true;
	}
	if (key < current.data) {
		newList = list.slice(0, midPoint);
		return binarySearch(newList, key);
	}
	if (key > current.data) {
		midPoint += 1;
		newlist = list.slice(midPoint);
		return binarySearch(newList, key);
	}
};

module.exports = binarySearch;
