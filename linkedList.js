class Node {
  constructor(data) {
    this.data = data;
    this.nextNode = undefined;
  }
}

class linkedList {
  constructor() {
    this.head = undefined;
  }

  //functional
  isEmpty() {
    // returns true if list is empty
    return this.head == undefined;
  }

  //functional
  emptyList() {
    // Empties the list [just for fun]
    return (this.head = undefined);
  }

  //functional
  sizeOf() {
    // returns the size of the list
    let current = this.head;
    let count = 0;

    while (current !== undefined) {
      count += 1;
      current = current.nextNode;
    }
    return count;
  }

  //functional
  has(key) {
    // function to check if the key exists in the list
    let current = this.head;
    while (current !== undefined) {
      if (current.data === key) {
        return true;
      } else {
        current = current.nextNode;
      }
    }

    return false;
  }

  //functional
  prepend(data) {
    // insert data to the beginning of the list
    let newNode = new Node(data);
    newNode.nextNode = this.head;
    this.head = newNode;
  }

  //functional
  append(data) {
    // insert data to the end of the list
    return this.insert(data, this.sizeOf());
  }

  //bug: only able to insert data at index 0. Throws invalid index error
  //cause: newNode wasn't declared before use
  //fixed
  insert(data, index = 0) {
    //insert data anywhere within the list. when no index argument is supplied behaves like the prepend function
    if (index === 0) {
      this.prepend(data);
    } else {
      try {
        let current = this.head;
        let count = index;

        while (count > 1) {
          current = current.nextNode;
          count -= 1;
        }

        let newNode = new Node(data);
        newNode.nextNode = current.nextNode;
        current.nextNode = newNode;
      } catch {
        return "Invalid Index";
      }
    }
  }

  //functional
  removeIndex(index = 0) {
    // removes and returns item at the index. when no index is supplied removes the most recent item added
    let current = this.head;

    try {
      if (index === 0) {
        //check index if 0 and replace the head with the next node from the head
        this.head = current.nextNode;
        return current;
      } else {
        let previous;
        let count = index;

        while (count > 0) {
          previous = current;
          current = current.nextNode;

          count -= 1;
        }

        previous.nextNode = current.nextNode;
        return current;
      }
    } catch {
      return "Invalid Index";
    }
  }

  // functional
  remove(key) {
    //removes and returns key if found in list

    let current = this.head;

    try {
      if (current.data === key && current === this.head) {
        this.head = current.nextNode;
        return current;
      } else {
        let previous;
        while (current.data !== key) {
          previous = current;
          current = current.nextNode;
        }

        previous.nextNode = current.nextNode;
        return current;
      }
    } catch {
      return "Invalid Key";
    }
  }

  //functional
  removeAll(key) {
    //removes all occurrences of key from list

    let size = this.sizeOf();
    while (size >= 0) {
      this.remove(key);
      size -= 1;
    }
  }

  //functional
  showAllNodes() {
    const size = this.sizeOf();
    let current = this.head;
    for (let i = 0; i < size; i++) {
      console.log("Index ", i, ": ", current);
      current = current.nextNode;
    }
  }
}
