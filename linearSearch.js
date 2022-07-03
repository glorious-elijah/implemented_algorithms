let linear_search = (list, target) => {
    for (let i = 0; i < list.length; i++) {
        if (target == list[i]) {
            return i;
        }
    }

    return -1;
};

let ad = linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10);
console.log(ad);
