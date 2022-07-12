const mergeSort = (list, rev = false) => {
  if (list.length <= 1) {
    return list;
  }

  let { leftHalf, rightHalf } = divide(list);
  let left = mergeSort(leftHalf, rev);
  let right = mergeSort(rightHalf, rev);

  return sort(left, right, rev);
};

const divide = (list) => {
  let mid = Math.floor(list.length / 2);
  let leftHalf = list.slice(0, mid);
  let rightHalf = list.slice(mid);

  return { leftHalf, rightHalf };
};

const sort = (arg1, arg2, rev) => {
  let newList = [];
  let i = 0;
  let j = 0;

  if (rev) {
    while (i < arg1.length && j < arg2.length) {
      if (arg1[i] > arg2[j]) {
        newList.push(arg1[i]);
        i += 1;
      } else {
        newList.push(arg2[j]);
        j += 1;
      }
    }
    while (i < arg1.length) {
      newList.push(arg1[i]);
      i += 1;
    }
    while (j < arg2.length) {
      newList.push(arg2[j]);
      j += 1;
    }

    return newList;
  } else {
    while (i < arg1.length && j < arg2.length) {
      if (arg1[i] < arg2[j]) {
        newList.push(arg1[i]);
        i += 1;
      } else {
        newList.push(arg2[j]);
        j += 1;
      }
    }
    while (i < arg1.length) {
      newList.push(arg1[i]);
      i += 1;
    }
    while (j < arg2.length) {
      newList.push(arg2[j]);
      j += 1;
    }

    return newList;
  }
};

d = mergeSort(
  [
    45, 22, 243, 234, 3, 4, 23, 4, 36, 234, 2, 45, 32, 3, 32, 324, 2, 564, 4,
    354, 3, 23,
  ],
  true
);

console.log(d);
