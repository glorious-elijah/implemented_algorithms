let binary_search = (sorted_list, target) => {
    let [first, last] = [0, sorted_list.length - 1];

    while (first <= last) {
        let mid = Math.floor((first + last) / 2);

        if (target === sorted_list[mid]) {
            return mid;
        } else if (target > sorted_list[mid]) {
            first = mid + 1;
        } else {
            last = mid - 1;
        }
    }
    return -1;
};

let ad = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4);
console.log(ad);
