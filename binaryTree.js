class Node {
	constructor(data) {
		this.data = data;
		this.right = null;
		this.left = null;
	}
}

class BinaryTree {
	constructor() {
		this.root = null;
	}

	insert(data) {
		let current = this.root;
		const DIRECTION = ["left", "right"];

		if (!current && current === this.root) {
			this.root = new Node(data);
			return;
		}
		while (current) {
			let index = Math.floor(Math.random() * 2);

			if (!current.left) {
				current.left = new Node(data);
				return;
			}
			if (!current.right) {
				current.right = new Node(data);
				return;
			}

			if (DIRECTION[index] === "left") {
				current = current.left;
			} else {
				current = current.right;
			}
		}
	}

	replaceRootRight(data) {
		const temp = this.root;
		this.root = new Node(data);
		this.root.right = temp;
	}

	replaceRootLeft(data) {
		const temp = this.root;
		this.root = new Node(data);
		this.root.left = temp;
	}

	insertRight(data) {
		let current = this.root;

		while (current) {
			if (!current.right) {
				break;
			}

			current = current.right;
		}

		current.right = new Node(data);
	}

	insertLeft(data) {
		let current = this.root;

		while (current) {
			if (!current.left) {
				break;
			}
			current = current.left;
		}

		current.left = new Node(data);
	}

	// inorderTraversal() {
	// 	//log out data in tree in left node, root, right node sequence
	// 	let current = this.root;
	// 	let pre;

	// 	while (current) {
	// 		//while current is not null
	// 		if (!current.left) {
	// 			// check if current.left is empty
	// 			console.log(current.data); //if current.left is empty display its data
	// 			current = current.right; // assign current to the current.right since we are at the end of the available left nodes
	// 		} else {
	// 			// if current.left is not empty
	// 			pre = current.left; // assign current.left to a new variable
	// 			while (pre.right && pre.right !== current) {
	// 				//loop till pre.right is null or pre.right is the same as current break out of loop otherwise
	// 				pre = pre.right; //while the condition is true assign the right node of the new variable to the variable
	// 			}
	// 			if (!pre.right) {
	// 				//check if pre.right is empty
	// 				pre.right = current; // if it is empty assign current from line 88 to pre.right
	// 				current = current.left; // reassign current to the left node of current from line 88 to pre
	// 			} else {
	// 				//if pre.right is not empty
	// 				pre.right = null; // reassign that node as empty
	// 				console.log(current.data); // log out current from line 88 data
	// 				current = current.right; // reassign current to current.right
	// 			}
	// 		}
	// 	}
	// }

	inorderTraversal(root, stack = []) {
		if (root) {
			this.inorderTraversal(root.left, stack);
			stack.push(root.data);
			this.inorderTraversal(root.right, stack);
		}

		return stack;
	}

	preorderTraversal(root, stack = []) {
		if (root) {
			stack.push(root.data);
			this.preorderTraversal(root.left, stack);
			this.preorderTraversal(root.right, stack);
		}

		return stack;
	}

	postorderTraversal(root, stack = []) {
		if (root) {
			this.postorderTraversal(root.left, stack);
			this.postorderTraversal(root.right, stack);
			stack.push(root.data);
		}

		return stack;
	}

	search(key) {
		const stack = this.inorderTraversal(this.root);
		return stack.some((value) => value === key);
	}
}

let d = new BinaryTree();
d.insert(1);
d.insert(2);
d.insert(3);
d.insert(4);
d.insert(5);

console.log(d.search(5));

// d.inorderTraversal();
// d.preorderTraversal();
