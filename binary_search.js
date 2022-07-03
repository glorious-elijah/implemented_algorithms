let binary_search = (list, target) => {
    let first = 0;
    let last = list.length - 1;

    while (first <= last) {
        let mid = Math.floor((first + last) / 2);
        if (target === list[mid]) {
            return mid;
        } else if (target > list[mid]) {
            first = mid + 1;
        } else {
            last = mid - 1;
        }
    }
    return -1;
};

let ad = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5);
console.log(ad);
