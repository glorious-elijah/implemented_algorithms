const linearSearch = (list, key) => {
	let current = list.head;

	for (let i = 0; i < list.sizeOf(); i++) {
		if (key === current.data) return true;
		current = current.nextNode;
	}

	return false;
};
