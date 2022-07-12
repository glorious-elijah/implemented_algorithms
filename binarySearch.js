const binary_search = (list, target) => {
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
